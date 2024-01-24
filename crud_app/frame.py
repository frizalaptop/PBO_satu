from tkinter import *
from tkinter import ttk
from siswa import Siswa
from tkinter import messagebox

class SimpleUI(Tk):
    def __init__(self):
        super().__init__()

        self.title("Simple UI with Tkinter Menu")
        self.geometry("400x300")

        # Membuat Menu Utama
        self.menu_utama = Menu(self)

        # Menu "Menu"
        menu_menu = Menu(self.menu_utama, tearoff=0)
        menu_menu.add_command(label="Semua Data Siswa", command=lambda: self.ganti_halaman(self.halaman_semua_data))
        menu_menu.add_command(label="Tambah Siswa", command=lambda: self.ganti_halaman(self.halaman_tambah_siswa))
        menu_menu.add_command(label="Ubah Siswa", command=lambda: self.ganti_halaman(self.halaman_ubah_siswa))
        menu_menu.add_command(label="Hapus Siswa", command=lambda: self.ganti_halaman(self.halaman_hapus_siswa))
        
        self.menu_utama.add_cascade(label="Menu", menu=menu_menu)

        # Menu "Keluar"
        self.menu_utama.add_command(label="Keluar", command=self.keluar)

        # Menetapkan Menu Utama ke Window
        self.config(menu=self.menu_utama)

        # Frame utama sebagai wadah konten
        self.frame_utama = Frame(self)
        self.frame_utama.pack(expand=True, fill="both")

        # Halaman default
        self.halaman_semua_data()

    def ganti_halaman(self, halaman):
        # Hapus konten pada frame utama
        for widget in self.frame_utama.winfo_children():
            widget.destroy()

        # Tampilkan halaman baru
        halaman()

    def halaman_semua_data(self):
        label = Label(self.frame_utama, text="Halaman Semua Data Siswa")
        label.pack(pady=20)

        # Create Treeview
        tree = ttk.Treeview(self.frame_utama, columns=("ID", "NIS", "Nama", "Kelas", "Gender"), show="headings")
        tree.heading("ID", text="ID Siswa", anchor="center")
        tree.heading("NIS", text="NIS", anchor="center")
        tree.heading("Nama", text="Nama", anchor="center")
        tree.heading("Kelas", text="Kelas", anchor="center")
        tree.heading("Gender", text="Gender", anchor="center")

        # Retrieve data from the database
        siswa = Siswa()
        data = siswa.lihat_siswa()

        # Insert data into the Treeview
        for row in data:
            tree.insert("", "end", values=row)
        for col in tree["columns"]:
            tree.column(col, anchor="center")

        tree.pack(pady=10)

    def halaman_tambah_siswa(self):
        label_nis = Label(self.frame_utama, text="NIS:")
        label_nis.grid(row=0, column=0, pady=5, padx=5, sticky=E)

        entry_nis = Entry(self.frame_utama)
        entry_nis.grid(row=0, column=1, pady=5, padx=5)

        label_nama = Label(self.frame_utama, text="Nama:")
        label_nama.grid(row=1, column=0, pady=5, padx=5, sticky=E)

        entry_nama = Entry(self.frame_utama)
        entry_nama.grid(row=1, column=1, pady=5, padx=5)

        label_kelas = Label(self.frame_utama, text="Kelas:")
        label_kelas.grid(row=2, column=0, pady=5, padx=5, sticky=E)

        kelas_options = ["1", "2", "3", "4", "5", "6"]
        selected_kelas = StringVar()
        kelas_dropdown = OptionMenu(self.frame_utama, selected_kelas, *kelas_options)
        kelas_dropdown.grid(row=2, column=1, pady=5, padx=5)

        label_gender = Label(self.frame_utama, text="Gender:")
        label_gender.grid(row=3, column=0, pady=5, padx=5, sticky=E)

        gender_options = ["L", "P"]
        selected_gender = StringVar()
        gender_dropdown = OptionMenu(self.frame_utama, selected_gender, *gender_options)
        gender_dropdown.grid(row=3, column=1, pady=5, padx=5)

        btn_simpan = Button(self.frame_utama, text="Simpan", command=lambda: self.simpan_siswa(entry_nis.get(), entry_nama.get(), selected_kelas.get(), selected_gender.get()))
        btn_simpan.grid(row=4, column=1, pady=10)

    def halaman_ubah_siswa(self):
        label_nis = Label(self.frame_utama, text="NIS:")
        label_nis.grid(row=0, column=0, pady=5, padx=5, sticky=E)

        entry_nis = Entry(self.frame_utama)
        entry_nis.grid(row=0, column=1, pady=5, padx=5)

        label_nama = Label(self.frame_utama, text="Nama:")
        label_nama.grid(row=1, column=0, pady=5, padx=5, sticky=E)

        entry_nama = Entry(self.frame_utama)
        entry_nama.grid(row=1, column=1, pady=5, padx=5)

        label_kelas = Label(self.frame_utama, text="Kelas:")
        label_kelas.grid(row=2, column=0, pady=5, padx=5, sticky=E)

        kelas_options = ["1", "2", "3", "4", "5", "6"]
        selected_kelas = StringVar()
        kelas_dropdown = OptionMenu(self.frame_utama, selected_kelas, *kelas_options)
        kelas_dropdown.grid(row=2, column=1, pady=5, padx=5)

        label_gender = Label(self.frame_utama, text="Gender:")
        label_gender.grid(row=3, column=0, pady=5, padx=5, sticky=E)

        gender_options = ["L", "P"]
        selected_gender = StringVar()
        gender_dropdown = OptionMenu(self.frame_utama, selected_gender, *gender_options)
        gender_dropdown.grid(row=3, column=1, pady=5, padx=5)

        btn_simpan = Button(self.frame_utama, text="Ubah", command=lambda: self.ubah_siswa(entry_nis.get(), entry_nama.get(), selected_kelas.get(), selected_gender.get()))
        btn_simpan.grid(row=4, column=1, pady=10)

    def halaman_hapus_siswa(self):
        label_nis = Label(self.frame_utama, text="NIS:")
        label_nis.grid(row=0, column=0, pady=5, padx=5, sticky=E)

        entry_nis = Entry(self.frame_utama)
        entry_nis.grid(row=0, column=1, pady=5, padx=5)

        btn_simpan = Button(self.frame_utama, text="Hapus", command=lambda: self.hapus_siswa(entry_nis.get()))
        btn_simpan.grid(row=4, column=1, pady=10)

    def keluar(self):
        self.destroy()

    def simpan_siswa(self, nis, nama, kelas, gender):
        if(not nis or not nama or not kelas or not gender):
            messagebox.showinfo("Gagal", "Data gagal di ubah")
            return False
        
        siswa = Siswa()
        siswa.nis = int(nis)
        siswa.nama = nama
        siswa.kelas = kelas
        siswa.gender = gender
        siswa.tambah_siswa()
        messagebox.showinfo("Simpan", "Data Siswa Tersimpan")
    
    def ubah_siswa(self, nis, nama, kelas, gender):
        if(not nis or not nama or not kelas or not gender):
            messagebox.showinfo("Gagal", "Data gagal di ubah")
            return False
        
        siswa = Siswa()
        siswa.nis = int(nis)
        siswa.nama = nama
        siswa.kelas = kelas
        siswa.gender = gender
        siswa.perbarui_siswa()
        messagebox.showinfo("Simpan", "Data Siswa Diubah")

    def hapus_siswa(self, nis):
        siswa = Siswa()
        siswa.nis = int(nis)
        siswa.hapus_siswa()
        messagebox.showinfo("Dihapus", "Data Siswa Dihapus")

if __name__ == "__main__":
    app = SimpleUI()
    app.mainloop()
