from tkinter import Frame,Label,Entry,Button,YES,BOTH,END,Tk,W,font
from math import pi

def titleFont():
    return font.Font(family='Helvetica', size=18, weight="bold")

def subTitleFont():
    return font.Font(family='Helvetica', size=12, weight="bold")

class KubusFrame(Frame):
    def __init__(self, master):
        super().__init__(master, bd=50)

        label = Label(self, text= "Halaman Kubus",font=titleFont())
        label.grid(row=0, column=0,columnspan=2, sticky='n', pady=30)

        volume_frame = Frame(self)
        volume_frame.grid(row=1, column=0, padx=30, sticky='n')

        Label(volume_frame, text="Menghitung Volume", font=subTitleFont()).grid(row=0, column=0,columnspan=2, sticky='n', pady=10)

        Label(volume_frame, text= "Rusuk: ").grid(row=1, column=0)

        self.txtRusuk1 = Entry(volume_frame, borderwidth=1, relief="solid")
        self.txtRusuk1.grid(row=1, column=1)

        self.txtvolume = Entry(volume_frame,font=("Helvetica", 10, "bold"))
        self.txtvolume.grid(row=3, column=0, columnspan=2,sticky='ew')

        Button(volume_frame, text="Hitung", command= self.result_volume, bg="#54B435", fg="white", font=("Helvetica", 10, "bold")).grid(row=2, column=0, columnspan=2,sticky='ew', pady=(10,0))

        luas_frame = Frame(self)
        luas_frame.grid(row=1, column=1, padx=30, sticky='n')

        Label(luas_frame, text="Menghitung Luas", font=subTitleFont()).grid(row=0, column=0,columnspan=2, sticky='n', pady=10)

        Label(luas_frame, text= "Rusuk: ").grid(row=1, column=0)

        self.txtRusuk2 = Entry(luas_frame, borderwidth=1, relief="solid")
        self.txtRusuk2.grid(row=1, column=1)
        
        self.txtLuas = Entry(luas_frame,font=("Helvetica", 10, "bold"))
        self.txtLuas.grid(row=4, column=0, columnspan=2,sticky='ew')

        Button(luas_frame, text="Hitung", command= self.result_luas, bg="#54B435", fg="white", font=("Helvetica", 10, "bold")).grid(row=3, column=0, columnspan=2,sticky='ew',pady=(10,0))

        ext_btn = Button(self, text="Kembali", command=lambda: master.main_page(), bg="#E64848", fg="white", font=("Helvetica", 10, "bold"))
        ext_btn.grid(row=2, column=0,columnspan=2, sticky='n', pady=30)

    def result_volume(self):
            self.txtvolume.delete(0, END)
            rusuk = float(self.txtRusuk1.get())
            volume = rusuk ** 3
            self.txtvolume.insert(0, f"volume = {volume:.2f}")

    def result_luas(self):
            self.txtLuas.delete(0, END)
            rusuk = float(self.txtRusuk2.get())
            luas = 6 * (rusuk ** 2)
            self.txtLuas.insert(0, f"Luas = {luas:.2f}")
        
class BalokFrame(Frame):
    def __init__(self, master):
        super().__init__(master, bd=50)
        label = Label(self, text= "Halaman Balok",font=titleFont())
        label.grid(row=0, column=0,columnspan=2, sticky='n', pady=30)

        volume_frame = Frame(self)
        volume_frame.grid(row=1, column=0, padx=30, sticky='n')

        Label(volume_frame, text="Menghitung Volume", font=subTitleFont()).grid(row=0, column=0,columnspan=2, sticky='n', pady=10)

        #todo
        Label(volume_frame, text= "Panjang: ").grid(row=1, column=0)
        Label(volume_frame, text="Lebar: ").grid(row=2, column=0)
        Label(volume_frame, text="Tinggi: ").grid(row=3, column=0)


        self.txtPanjang1 = Entry(volume_frame, borderwidth=1, relief="solid")
        self.txtPanjang1.grid(row=1, column=1)
        self.txtLebar1 = Entry(volume_frame, borderwidth=1, relief="solid")
        self.txtLebar1.grid(row=2, column=1)
        self.txtTinggi1 = Entry(volume_frame, borderwidth=1, relief="solid")
        self.txtTinggi1.grid(row=3, column=1)
        #end
        
        self.txtvolume = Entry(volume_frame,font=("Helvetica", 10, "bold"))
        self.txtvolume.grid(row=5, column=0, columnspan=2,sticky='ew')

        Button(volume_frame, text="Hitung", command= self.result_volume, bg="#54B435", fg="white", font=("Helvetica", 10, "bold")).grid(row=4, column=0, columnspan=2,sticky='ew', pady=(10,0))

        luas_frame = Frame(self)
        luas_frame.grid(row=1, column=1, padx=30, sticky='n')

        Label(luas_frame, text="Menghitung Luas", font=subTitleFont()).grid(row=0, column=0,columnspan=2, sticky='n', pady=10)

        #todo
        Label(luas_frame, text= "Panjang: ").grid(row=1, column=0)
        Label(luas_frame, text="Lebar: ").grid(row=2, column=0)
        Label(luas_frame, text="Tinggi: ").grid(row=3, column=0)

        self.txtPanjang2 = Entry(luas_frame, borderwidth=1, relief="solid")
        self.txtPanjang2.grid(row=1, column=1)
        self.txtLebar2 = Entry(luas_frame, borderwidth=1, relief="solid")
        self.txtLebar2.grid(row=2, column=1)
        self.txtTinggi2 = Entry(luas_frame, borderwidth=1, relief="solid")
        self.txtTinggi2.grid(row=3, column=1)
        #end

        self.txtLuas = Entry(luas_frame,font=("Helvetica", 10, "bold"))
        self.txtLuas.grid(row=5, column=0, columnspan=2,sticky='ew')

        Button(luas_frame, text="Hitung", command= self.result_luas, bg="#54B435", fg="white", font=("Helvetica", 10, "bold")).grid(row=4, column=0, columnspan=2,sticky='ew',pady=(10,0))

        ext_btn = Button(self, text="Kembali", command=lambda: master.main_page(), bg="#E64848", fg="white", font=("Helvetica", 10, "bold"))
        ext_btn.grid(row=2, column=0,columnspan=2, sticky='n', pady=30)

    def result_volume(self):
            self.txtvolume.delete(0, END)
            panjang = float(self.txtPanjang1.get())
            lebar = float(self.txtLebar1.get())
            tinggi = float(self.txtTinggi1.get())
            volume = panjang * lebar * tinggi
            self.txtvolume.insert(0, f"volume = {volume:.2f}")

    def result_luas(self):
            self.txtLuas.delete(0, END)
            panjang = float(self.txtPanjang2.get())
            lebar = float(self.txtLebar2.get())
            tinggi = float(self.txtTinggi2.get())
            luas = (2*panjang*lebar) + (2*panjang*tinggi) + (2*lebar*tinggi)
            self.txtLuas.insert(0, f"Luas = {luas:.2f}")

class LimasSegiempatFrame(Frame):
    def __init__(self, master):
        super().__init__(master, bd=50)
        label = Label(self, text= "Halaman Limas Segiempat",font=titleFont())
        label.grid(row=0, column=0,columnspan=2, sticky='n', pady=30)

        volume_frame = Frame(self)
        volume_frame.grid(row=1, column=0, padx=30, sticky='n')

        Label(volume_frame, text="Menghitung Volume", font=subTitleFont()).grid(row=0, column=0,columnspan=2, sticky='n', pady=10)

        #todo
        Label(volume_frame, text= "Luas Alas: ").grid(row=1, column=0)
        Label(volume_frame, text="Tinggi: ").grid(row=2, column=0)

        self.txtLuasAlas = Entry(volume_frame, borderwidth=1, relief="solid")
        self.txtLuasAlas.grid(row=1, column=1)
        self.txtTinggi = Entry(volume_frame, borderwidth=1, relief="solid")
        self.txtTinggi.grid(row=2, column=1)
        #end

        self.txtvolume = Entry(volume_frame,font=("Helvetica", 10, "bold"))
        self.txtvolume.grid(row=4, column=0, columnspan=2,sticky='ew')

        Button(volume_frame, text="Hitung", command= self.result_volume, bg="#54B435", fg="white", font=("Helvetica", 10, "bold")).grid(row=3, column=0, columnspan=2,sticky='ew', pady=(79,0))

        luas_frame = Frame(self)
        luas_frame.grid(row=1, column=1, padx=30, sticky='n')

        Label(luas_frame, text="Menghitung Luas", font=subTitleFont()).grid(row=0, column=0,columnspan=2, sticky='n', pady=10)

        #todo
        Label(luas_frame, text= "Luas Sisi A: ").grid(row=1, column=0)
        Label(luas_frame, text= "Luas Sisi B: ").grid(row=2, column=0)
        Label(luas_frame, text= "Luas Sisi C: ").grid(row=3, column=0)
        Label(luas_frame, text= "Luas Sisi D: ").grid(row=4, column=0)
        Label(luas_frame, text= "Luas Sisi E: ").grid(row=5, column=0)

        self.txtLuasA = Entry(luas_frame, borderwidth=1, relief="solid")
        self.txtLuasA.grid(row=1, column=1)
        self.txtLuasB = Entry(luas_frame, borderwidth=1, relief="solid")
        self.txtLuasB.grid(row=2, column=1)
        self.txtLuasC = Entry(luas_frame, borderwidth=1, relief="solid")
        self.txtLuasC.grid(row=3, column=1)
        self.txtLuasD = Entry(luas_frame, borderwidth=1, relief="solid")
        self.txtLuasD.grid(row=4, column=1)
        self.txtLuasE = Entry(luas_frame, borderwidth=1, relief="solid")
        self.txtLuasE.grid(row=5, column=1)
        #end

        self.txtLuas = Entry(luas_frame,font=("Helvetica", 10, "bold"))
        self.txtLuas.grid(row=7, column=0, columnspan=2,sticky='ew')

        Button(luas_frame, text="Hitung", command= self.result_luas, bg="#54B435", fg="white", font=("Helvetica", 10, "bold")).grid(row=6, column=0, columnspan=2,sticky='ew',pady=(10,0))

        ext_btn = Button(self, text="Kembali", command=lambda: master.main_page(), bg="#E64848", fg="white", font=("Helvetica", 10, "bold"))
        ext_btn.grid(row=2, column=0,columnspan=2, sticky='n', pady=30)

    def result_volume(self):
            self.txtvolume.delete(0, END)
            la = float(self.txtLuasAlas.get())
            t = float(self.txtTinggi.get())
            volume = (la * t) / 3
            self.txtvolume.insert(0, f"volume = {volume:.2f}")

    def result_luas(self):
            self.txtLuas.delete(0, END)
            a = float(self.txtLuasA.get())
            b = float(self.txtLuasB.get())
            c = float(self.txtLuasC.get())
            d = float(self.txtLuasD.get())
            e = float(self.txtLuasE.get())
            luas = a+b+c+d+e
            self.txtLuas.insert(0, f"Luas = {luas:.2f}")

class PrismaSegitigaFrame(Frame):
    def __init__(self, master):
        super().__init__(master, bd=50)
        label = Label(self, text= "Halaman PrismaSegitiga",font=titleFont())
        label.grid(row=0, column=0,columnspan=2, sticky='n', pady=30)

        volume_frame = Frame(self)
        volume_frame.grid(row=1, column=0, padx=30, sticky='n')

        Label(volume_frame, text="Menghitung Volume", font=subTitleFont()).grid(row=0, column=0,columnspan=2, sticky='n', pady=10)

        #todo
        Label(volume_frame, text= "Luas: ").grid(row=1, column=0)
        Label(volume_frame, text="Tinggi: ").grid(row=2, column=0)

        self.txtLuas1 = Entry(volume_frame, borderwidth=1, relief="solid")
        self.txtLuas1.grid(row=1, column=1)
        self.txtTinggi1 = Entry(volume_frame, borderwidth=1, relief="solid")
        self.txtTinggi1.grid(row=2, column=1)
        #end

        self.txtvolume = Entry(volume_frame,font=("Helvetica", 10, "bold"))
        self.txtvolume.grid(row=4, column=0, columnspan=2,sticky='ew')

        Button(volume_frame, text="Hitung", command= self.result_volume, bg="#54B435", fg="white", font=("Helvetica", 10, "bold")).grid(row=3, column=0, columnspan=2,sticky='ew', pady=(79,0))

        luas_frame = Frame(self)
        luas_frame.grid(row=1, column=1, padx=30, sticky='n')

        Label(luas_frame, text="Menghitung Luas", font=subTitleFont()).grid(row=0, column=0,columnspan=2, sticky='n', pady=10)

        #todo
        Label(luas_frame, text= "Sisi A: ").grid(row=1, column=0)
        Label(luas_frame, text= "Sisi B: ").grid(row=2, column=0)
        Label(luas_frame, text= "Sisi C: ").grid(row=3, column=0)
        Label(luas_frame, text= "Luas: ").grid(row=4, column=0)
        Label(luas_frame, text="Tinggi: ").grid(row=5, column=0)

        self.txtSisiA = Entry(luas_frame, borderwidth=1, relief="solid")
        self.txtSisiA.grid(row=1, column=1)
        self.txtSisiB = Entry(luas_frame, borderwidth=1, relief="solid")
        self.txtSisiB.grid(row=2, column=1)
        self.txtSisiC = Entry(luas_frame, borderwidth=1, relief="solid")
        self.txtSisiC.grid(row=3, column=1)
        self.txtLuas2 = Entry(luas_frame, borderwidth=1, relief="solid")
        self.txtLuas2.grid(row=4, column=1)
        self.txtTinggi2 = Entry(luas_frame, borderwidth=1, relief="solid")
        self.txtTinggi2.grid(row=5, column=1)
        #end

        self.txtLuas = Entry(luas_frame,font=("Helvetica", 10, "bold"))
        self.txtLuas.grid(row=7, column=0, columnspan=2,sticky='ew')

        Button(luas_frame, text="Hitung", command= self.result_luas, bg="#54B435", fg="white", font=("Helvetica", 10, "bold")).grid(row=6, column=0, columnspan=2,sticky='ew',pady=(10,0))

        ext_btn = Button(self, text="Kembali", command=lambda: master.main_page(), bg="#E64848", fg="white", font=("Helvetica", 10, "bold"))
        ext_btn.grid(row=2, column=0,columnspan=2, sticky='n', pady=30)

    def result_volume(self):
            self.txtvolume.delete(0, END)
            l = float(self.txtLuas1.get())
            t = float(self.txtTinggi1.get())
            volume = (l * t) / 2
            self.txtvolume.insert(0, f"volume = {volume:.2f}")

    def result_luas(self):
            self.txtLuas.delete(0, END)
            sisiA = float(self.txtSisiA.get())
            sisiB = float(self.txtSisiB.get())
            sisiC = float(self.txtSisiC.get())
            t = float(self.txtTinggi2.get())
            l = float(self.txtLuas2.get())
            luas = (sisiA+sisiB+sisiC)*t+l
            self.txtLuas.insert(0, f"Luas = {luas:.2f}")

class LimasSegitiga(Frame):
    def __init__(self, master):
        super().__init__(master, bd=50)
        label = Label(self, text= "Halaman Limas Segitiga",font=titleFont())
        label.grid(row=0, column=0,columnspan=2, sticky='n', pady=30)

        volume_frame = Frame(self)
        volume_frame.grid(row=1, column=0, padx=30, sticky='n')

        Label(volume_frame, text="Menghitung Volume", font=subTitleFont()).grid(row=0, column=0,columnspan=2, sticky='n', pady=10)

        #todo
        Label(volume_frame, text= "Luas: ").grid(row=1, column=0)
        Label(volume_frame, text= "Tinggi: ").grid(row=2, column=0)

        self.txtLuas1 = Entry(volume_frame, borderwidth=1, relief="solid")
        self.txtLuas1.grid(row=1, column=1)
        self.txtTinggi1 = Entry(volume_frame, borderwidth=1, relief="solid")
        self.txtTinggi1.grid(row=2, column=1)
        #end

        self.txtvolume = Entry(volume_frame,font=("Helvetica", 10, "bold"))
        self.txtvolume.grid(row=4, column=0, columnspan=2,sticky='ew')

        Button(volume_frame, text="Hitung", command= self.result_volume, bg="#54B435", fg="white", font=("Helvetica", 10, "bold")).grid(row=3, column=0, columnspan=2,sticky='ew', pady=(57,0))

        luas_frame = Frame(self)
        luas_frame.grid(row=1, column=1, padx=30, sticky='n')

        Label(luas_frame, text="Menghitung Luas", font=subTitleFont()).grid(row=0, column=0,columnspan=2, sticky='n', pady=10)

        #todo
        Label(luas_frame, text= "Luas Sisi A: ").grid(row=1, column=0)
        Label(luas_frame, text= "Luas Sisi B: ").grid(row=2, column=0)
        Label(luas_frame, text= "Luas Sisi C: ").grid(row=3, column=0)
        Label(luas_frame, text= "Luas Sisi D: ").grid(row=4, column=0)

        self.txtLuasA = Entry(luas_frame, borderwidth=1, relief="solid")
        self.txtLuasA.grid(row=1, column=1)
        self.txtLuasB = Entry(luas_frame, borderwidth=1, relief="solid")
        self.txtLuasB.grid(row=2, column=1)
        self.txtLuasC = Entry(luas_frame, borderwidth=1, relief="solid")
        self.txtLuasC.grid(row=3, column=1)
        self.txtLuasD = Entry(luas_frame, borderwidth=1, relief="solid")
        self.txtLuasD.grid(row=4, column=1)
        #end

        self.txtLuas = Entry(luas_frame,font=("Helvetica", 10, "bold"))
        self.txtLuas.grid(row=6, column=0, columnspan=2,sticky='ew')

        Button(luas_frame, text="Hitung", command= self.result_luas, bg="#54B435", fg="white", font=("Helvetica", 10, "bold")).grid(row=5, column=0, columnspan=2,sticky='ew',pady=(10,0))

        ext_btn = Button(self, text="Kembali", command=lambda: master.main_page(), bg="#E64848", fg="white", font=("Helvetica", 10, "bold"))
        ext_btn.grid(row=2, column=0,columnspan=2, sticky='n', pady=30)

    def result_volume(self):
            self.txtvolume.delete(0, END)
            l = float(self.txtLuas1.get())
            t = float(self.txtTinggi1.get())
            volume = (l*t)/6
            self.txtvolume.insert(0, f"volume = {volume:.2f}")

    def result_luas(self):
            self.txtLuas.delete(0, END)
            a = float(self.txtLuasA.get())
            b = float(self.txtLuasB.get())
            c = float(self.txtLuasC.get())
            d = float(self.txtLuasD.get())
            luas = a+b+c+d
            self.txtLuas.insert(0, f"Luas = {luas:.2f}")

class Silinder(Frame):
    def __init__(self, master):
        super().__init__(master, bd=50)
        label = Label(self, text= "Halaman Silinder",font=titleFont())
        label.grid(row=0, column=0,columnspan=2, sticky='n', pady=30)

        volume_frame = Frame(self)
        volume_frame.grid(row=1, column=0, padx=30, sticky='n')

        Label(volume_frame, text="Menghitung Volume", font=subTitleFont()).grid(row=0, column=0,columnspan=2, sticky='n', pady=10)

        #todo
        Label(volume_frame, text= "Jari-jari ").grid(row=1, column=0)
        Label(volume_frame, text="Tinggi: ").grid(row=2, column=0)

        self.txtJr1 = Entry(volume_frame, borderwidth=1, relief="solid")
        self.txtJr1.grid(row=1, column=1)
        self.txtTinggi1 = Entry(volume_frame, borderwidth=1, relief="solid")
        self.txtTinggi1.grid(row=2, column=1)
        #end

        self.txtvolume = Entry(volume_frame,font=("Helvetica", 10, "bold"))
        self.txtvolume.grid(row=4, column=0, columnspan=2,sticky='ew')

        Button(volume_frame, text="Hitung", command= self.result_volume, bg="#54B435", fg="white", font=("Helvetica", 10, "bold")).grid(row=3, column=0, columnspan=2,sticky='ew', pady=(10,0))

        luas_frame = Frame(self)
        luas_frame.grid(row=1, column=1, padx=30, sticky='n')

        Label(luas_frame, text="Menghitung Luas", font=subTitleFont()).grid(row=0, column=0,columnspan=2, sticky='n', pady=10)

        #todo
        Label(luas_frame, text= "Jari-jari ").grid(row=1, column=0)
        Label(luas_frame, text="Tinggi: ").grid(row=2, column=0)

        self.txtJr2 = Entry(luas_frame, borderwidth=1, relief="solid")
        self.txtJr2.grid(row=1, column=1)
        self.txtTinggi2 = Entry(luas_frame, borderwidth=1, relief="solid")
        self.txtTinggi2.grid(row=2, column=1)
        #end

        self.txtLuasSelimut = Entry(luas_frame,font=("Helvetica", 10, "bold"))
        self.txtLuasSelimut.grid(row=4, column=0, columnspan=2,sticky='ew')
        self.txtLuasPermukaan = Entry(luas_frame,font=("Helvetica", 10, "bold"))
        self.txtLuasPermukaan.grid(row=5, column=0, columnspan=2,sticky='ew')

        Button(luas_frame, text="Hitung", command= self.result_luas, bg="#54B435", fg="white", font=("Helvetica", 10, "bold")).grid(row=3, column=0, columnspan=2,sticky='ew', pady=(10,0))

        ext_btn = Button(self, text="Kembali", command=lambda: master.main_page(), bg="#E64848", fg="white", font=("Helvetica", 10, "bold"))
        ext_btn.grid(row=2, column=0,columnspan=2, sticky='n', pady=30)

    def result_volume(self):
            self.txtvolume.delete(0, END)
            jr = float(self.txtJr1.get())
            t = float(self.txtTinggi1.get())
            volume = pi * (jr ** 2) * t
            self.txtvolume.insert(0, f"volume = {volume:.2f}")

    def result_luas(self):
            self.txtLuasSelimut.delete(0, END)
            self.txtLuasPermukaan.delete(0, END)
            jr = float(self.txtJr2.get())
            t = float(self.txtTinggi2.get())
            luasSelimut = 2*pi*jr*t
            luasPermukaan = (2*pi*jr*t) + (2*pi*(jr**2)*t)
            self.txtLuasSelimut.insert(0, f"Luas Selimut = {luasSelimut:.2f}")  
            self.txtLuasPermukaan.insert(0, f"Luas Permukaan = {luasPermukaan:.2f}")  

class Bola(Frame):
    def __init__(self, master):
        super().__init__(master, bd=50)
        label = Label(self, text= "Halaman Bola",font=titleFont())
        label.grid(row=0, column=0,columnspan=2, sticky='n', pady=30)

        volume_frame = Frame(self)
        volume_frame.grid(row=1, column=0, padx=30, sticky='n')

        Label(volume_frame, text="Menghitung Volume", font=subTitleFont()).grid(row=0, column=0,columnspan=2, sticky='n', pady=10)

        #todo
        Label(volume_frame, text= "Jari-jari: ").grid(row=1, column=0)

        self.txtJr1 = Entry(volume_frame, borderwidth=1, relief="solid")
        self.txtJr1.grid(row=1, column=1)
        #end

        self.txtvolume = Entry(volume_frame,font=("Helvetica", 10, "bold"))
        self.txtvolume.grid(row=3, column=0, columnspan=2,sticky='ew')

        Button(volume_frame, text="Hitung", command= self.result_volume, bg="#54B435", fg="white", font=("Helvetica", 10, "bold")).grid(row=2, column=0, columnspan=2,sticky='ew', pady=(10,0))

        luas_frame = Frame(self)
        luas_frame.grid(row=1, column=1, padx=30, sticky='n')

        Label(luas_frame, text="Menghitung Luas", font=subTitleFont()).grid(row=0, column=0,columnspan=2, sticky='n', pady=10)

        #todo
        Label(luas_frame, text= "Jari-jari: ").grid(row=1, column=0)

        self.txtJr2 = Entry(luas_frame, borderwidth=1, relief="solid")
        self.txtJr2.grid(row=1, column=1)
        #end

        self.txtLuas = Entry(luas_frame,font=("Helvetica", 10, "bold"))
        self.txtLuas.grid(row=3, column=0, columnspan=2,sticky='ew')

        Button(luas_frame, text="Hitung", command= self.result_luas, bg="#54B435", fg="white", font=("Helvetica", 10, "bold")).grid(row=2, column=0, columnspan=2,sticky='ew', pady=(10,0))

        ext_btn = Button(self, text="Kembali", command=lambda: master.main_page(), bg="#E64848", fg="white", font=("Helvetica", 10, "bold"))
        ext_btn.grid(row=2, column=0,columnspan=2, sticky='n', pady=30)

    def result_volume(self):
            self.txtvolume.delete(0, END)
            jr = float(self.txtJr1.get())
            volume = (4/3)*pi*(jr**3)
            self.txtvolume.insert(0, f"volume = {volume:.2f}")

    def result_luas(self):
            self.txtLuas.delete(0, END)
            jr = float(self.txtJr2.get())
            luas = (4/3)*pi*(jr**2)
            self.txtLuas.insert(0, f"Luas = {luas:.2f}")   

           



class Parent(Tk):
    def __init__(self):
        super().__init__()
        self.title("Bangun Ruang")
        self.currentFrame = MainPage(self)
        self.currentFrame.pack(expand=YES)   

    def show_page(self,i):
        for index, page in enumerate(self.pageNames):
            if page.__name__ == i:
                self.currentFrame.destroy()
                self.currentFrame = page(self)
                self.currentFrame.pack(expand=YES)

    def main_page(self):
        self.currentFrame.destroy()
        self.currentFrame = MainPage(self)
        self.currentFrame.pack(expand=YES)

    pageNames = [KubusFrame, BalokFrame,LimasSegiempatFrame, PrismaSegitigaFrame, LimasSegitiga, Silinder, Bola]
            
class MainPage(Frame):
    def __init__(self, master):
        super().__init__(master, bd=30 )
        label = Label(self, text= "Pilih bangun ruang yang ingin anda hitung luas atau volumenya", font=titleFont())
        label.pack()

        buttons = [
            ("Kubus", 0, 0), ("Balok",0,1),
            ("Limas Segiempat",1,0), ("Prisma Segitiga",1,1),
            ("Limas Segitiga",2,0), ("Silinder",2,1),
            ("Bola",3,0)
        ]

        button_frame = Frame(self)
        button_frame.pack()

        for index, button_text in enumerate(buttons):
            button = Button(button_frame, text=button_text[0],width=20, command=lambda idx=index: master.show_page(master.pageNames[idx].__name__))
            button.grid(row=button_text[1], column=button_text[2], padx=15, pady=15)
            button.bind("<Enter>",lambda event,button=button: self.on_enter(event, button))
            button.configure(bg='#F4DFB6', font=('Helvetica', 10, 'normal'))
            button.bind("<Leave>",lambda event, button=button: self.on_leave(event, button))
            

    def on_enter(self, event, button):
        button.configure(bg='lightblue', font=('Helvetica', 10, 'bold'))

    def on_leave(self, event, button):
        button.configure(bg='#F4DFB6', font=('Helvetica', 10, 'normal'))

app = Parent()
app.minsize(800, 400)
app.mainloop()