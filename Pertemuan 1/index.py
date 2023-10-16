from tkinter import Frame,Label,Entry,Button,YES,BOTH,END,Tk,W,font
def titleFont():
    return font.Font(family='Helvetica', size=18, weight="bold")

def subTitleFont():
    return font.Font(family='Helvetica', size=12, weight="bold")

class PersegiFrame(Frame):
    def __init__(self, master):
        super().__init__(master, bd=50)

        label = Label(self, text= "Halaman Persegi",font=titleFont())
        label.grid(row=0, column=0,columnspan=2, sticky='n', pady=30)

        keliling_frame = Frame(self)
        keliling_frame.grid(row=1, column=0, padx=30, sticky='n')

        Label(keliling_frame, text="Menghitung Keliling", font=subTitleFont()).grid(row=0, column=0,columnspan=2, sticky='n', pady=10)

        Label(keliling_frame, text= "Sisi: ").grid(row=1, column=0)

        self.txtSisi1 = Entry(keliling_frame, borderwidth=1, relief="solid")
        self.txtSisi1.grid(row=1, column=1)

        self.txtKeliling = Entry(keliling_frame,font=("Helvetica", 10, "bold"))
        self.txtKeliling.grid(row=3, column=0, columnspan=2,sticky='ew')

        Button(keliling_frame, text="Hitung", command= self.result_keliling, bg="#54B435", fg="white", font=("Helvetica", 10, "bold")).grid(row=2, column=0, columnspan=2,sticky='ew', pady=(10,0))

        luas_frame = Frame(self)
        luas_frame.grid(row=1, column=1, padx=30, sticky='n')

        Label(luas_frame, text="Menghitung Luas", font=subTitleFont()).grid(row=0, column=0,columnspan=2, sticky='n', pady=10)

        Label(luas_frame, text= "Sisi: ").grid(row=1, column=0)

        self.txtSisi2 = Entry(luas_frame, borderwidth=1, relief="solid")
        self.txtSisi2.grid(row=1, column=1)
        
        self.txtLuas = Entry(luas_frame,font=("Helvetica", 10, "bold"))
        self.txtLuas.grid(row=4, column=0, columnspan=2,sticky='ew')

        Button(luas_frame, text="Hitung", command= self.result_luas, bg="#54B435", fg="white", font=("Helvetica", 10, "bold")).grid(row=3, column=0, columnspan=2,sticky='ew',pady=(10,0))

        ext_btn = Button(self, text="Kembali", command=lambda: master.main_page(), bg="#E64848", fg="white", font=("Helvetica", 10, "bold"))
        ext_btn.grid(row=2, column=0,columnspan=2, sticky='n', pady=30)

    def result_keliling(self):
            self.txtKeliling.delete(0, END)
            sisi = float(self.txtSisi1.get())
            keliling = sisi*4
            self.txtKeliling.insert(0, f"Keliling = {keliling}")

    def result_luas(self):
            self.txtLuas.delete(0, END)
            sisi = float(self.txtSisi2.get())
            luas = sisi*sisi
            self.txtLuas.insert(0, f"Luas = {luas}")
        
class PersegiPanjangFrame(Frame):
    def __init__(self, master):
        super().__init__(master, bd=50)
        label = Label(self, text= "Halaman Persegi Panjang",font=titleFont())
        label.grid(row=0, column=0,columnspan=2, sticky='n', pady=30)

        keliling_frame = Frame(self)
        keliling_frame.grid(row=1, column=0, padx=30, sticky='n')

        Label(keliling_frame, text="Menghitung Keliling", font=subTitleFont()).grid(row=0, column=0,columnspan=2, sticky='n', pady=10)

        #todo
        Label(keliling_frame, text= "Panjang: ").grid(row=1, column=0)
        Label(keliling_frame, text="Lebar: ").grid(row=2, column=0)

        self.txtPanjang1 = Entry(keliling_frame, borderwidth=1, relief="solid")
        self.txtPanjang1.grid(row=1, column=1)
        self.txtLebar1 = Entry(keliling_frame, borderwidth=1, relief="solid")
        self.txtLebar1.grid(row=2, column=1)
        #end
        
        self.txtKeliling = Entry(keliling_frame,font=("Helvetica", 10, "bold"))
        self.txtKeliling.grid(row=4, column=0, columnspan=2,sticky='ew')

        Button(keliling_frame, text="Hitung", command= self.result_keliling, bg="#54B435", fg="white", font=("Helvetica", 10, "bold")).grid(row=3, column=0, columnspan=2,sticky='ew', pady=(10,0))

        luas_frame = Frame(self)
        luas_frame.grid(row=1, column=1, padx=30, sticky='n')

        Label(luas_frame, text="Menghitung Luas", font=subTitleFont()).grid(row=0, column=0,columnspan=2, sticky='n', pady=10)

        #todo
        Label(luas_frame, text= "Panjang: ").grid(row=1, column=0)
        Label(luas_frame, text="Lebar: ").grid(row=2, column=0)

        self.txtPanjang2 = Entry(luas_frame, borderwidth=1, relief="solid")
        self.txtPanjang2.grid(row=1, column=1)
        self.txtLebar2 = Entry(luas_frame, borderwidth=1, relief="solid")
        self.txtLebar2.grid(row=2, column=1)
        #end

        self.txtLuas = Entry(luas_frame,font=("Helvetica", 10, "bold"))
        self.txtLuas.grid(row=4, column=0, columnspan=2,sticky='ew')

        Button(luas_frame, text="Hitung", command= self.result_luas, bg="#54B435", fg="white", font=("Helvetica", 10, "bold")).grid(row=3, column=0, columnspan=2,sticky='ew',pady=(10,0))

        ext_btn = Button(self, text="Kembali", command=lambda: master.main_page(), bg="#E64848", fg="white", font=("Helvetica", 10, "bold"))
        ext_btn.grid(row=2, column=0,columnspan=2, sticky='n', pady=30)

    def result_keliling(self):
            self.txtKeliling.delete(0, END)
            panjang = float(self.txtPanjang1.get())
            lebar = float(self.txtLebar1.get())
            keliling = 2 * (panjang + lebar)
            self.txtKeliling.insert(0, f"Keliling = {keliling}")

    def result_luas(self):
            self.txtLuas.delete(0, END)
            panjang = float(self.txtPanjang2.get())
            lebar = float(self.txtLebar2.get())
            luas = panjang*lebar
            self.txtLuas.insert(0, f"Luas = {luas}")

class JajarGenjangFrame(Frame):
    def __init__(self, master):
        super().__init__(master, bd=50)
        label = Label(self, text= "Halaman Jajar Genjang",font=titleFont())
        label.grid(row=0, column=0,columnspan=2, sticky='n', pady=30)

        keliling_frame = Frame(self)
        keliling_frame.grid(row=1, column=0, padx=30, sticky='n')

        Label(keliling_frame, text="Menghitung Keliling", font=subTitleFont()).grid(row=0, column=0,columnspan=2, sticky='n', pady=10)

        #todo
        Label(keliling_frame, text= "Sisi A: ").grid(row=1, column=0)
        Label(keliling_frame, text="Sisi B: ").grid(row=2, column=0)
        Label(keliling_frame, text= "Sisi C: ").grid(row=3, column=0)
        Label(keliling_frame, text="Sisi D: ").grid(row=4, column=0)

        self.txtSisiA = Entry(keliling_frame, borderwidth=1, relief="solid")
        self.txtSisiA.grid(row=1, column=1)
        self.txtSisiB = Entry(keliling_frame, borderwidth=1, relief="solid")
        self.txtSisiB.grid(row=2, column=1)
        self.txtSisiC = Entry(keliling_frame, borderwidth=1, relief="solid")
        self.txtSisiC.grid(row=3, column=1)
        self.txtSisiD = Entry(keliling_frame, borderwidth=1, relief="solid")
        self.txtSisiD.grid(row=4, column=1)
        #end

        self.txtKeliling = Entry(keliling_frame,font=("Helvetica", 10, "bold"))
        self.txtKeliling.grid(row=6, column=0, columnspan=2,sticky='ew')

        Button(keliling_frame, text="Hitung", command= self.result_keliling, bg="#54B435", fg="white", font=("Helvetica", 10, "bold")).grid(row=5, column=0, columnspan=2,sticky='ew', pady=(10,0))

        luas_frame = Frame(self)
        luas_frame.grid(row=1, column=1, padx=30, sticky='n')

        Label(luas_frame, text="Menghitung Luas", font=subTitleFont()).grid(row=0, column=0,columnspan=2, sticky='n', pady=10)

        #todo
        Label(luas_frame, text= "Alas: ").grid(row=1, column=0)
        Label(luas_frame, text= "Tinggi: ").grid(row=2, column=0)

        self.txtAlas = Entry(luas_frame, borderwidth=1, relief="solid")
        self.txtAlas.grid(row=1, column=1)
        self.txtTinggi = Entry(luas_frame, borderwidth=1, relief="solid")
        self.txtTinggi.grid(row=2, column=1)
        #end

        self.txtLuas = Entry(luas_frame,font=("Helvetica", 10, "bold"))
        self.txtLuas.grid(row=4, column=0, columnspan=2,sticky='ew')

        Button(luas_frame, text="Hitung", command= self.result_luas, bg="#54B435", fg="white", font=("Helvetica", 10, "bold")).grid(row=3, column=0, columnspan=2,sticky='ew',pady=(53,0))

        ext_btn = Button(self, text="Kembali", command=lambda: master.main_page(), bg="#E64848", fg="white", font=("Helvetica", 10, "bold"))
        ext_btn.grid(row=2, column=0,columnspan=2, sticky='n', pady=30)

    def result_keliling(self):
            self.txtKeliling.delete(0, END)
            a = float(self.txtSisiA.get())
            b = float(self.txtSisiB.get())
            c = float(self.txtSisiC.get())
            d = float(self.txtSisiD.get())
            keliling = a+b+c+d
            self.txtKeliling.insert(0, f"Keliling = {keliling}")

    def result_luas(self):
            self.txtLuas.delete(0, END)
            alas = float(self.txtAlas.get())
            tinggi = float(self.txtTinggi.get())
            luas = alas*tinggi
            self.txtLuas.insert(0, f"Luas = {luas}")

class SegitigaFrame(Frame):
    def __init__(self, master):
        super().__init__(master, bd=50)
        label = Label(self, text= "Halaman Segitiga",font=titleFont())
        label.grid(row=0, column=0,columnspan=2, sticky='n', pady=30)

        keliling_frame = Frame(self)
        keliling_frame.grid(row=1, column=0, padx=30, sticky='n')

        Label(keliling_frame, text="Menghitung Keliling", font=subTitleFont()).grid(row=0, column=0,columnspan=2, sticky='n', pady=10)

        #todo
        Label(keliling_frame, text= "Sisi A: ").grid(row=1, column=0)
        Label(keliling_frame, text="Sisi B: ").grid(row=2, column=0)
        Label(keliling_frame, text= "Sisi C: ").grid(row=3, column=0)

        self.txtSisiA = Entry(keliling_frame, borderwidth=1, relief="solid")
        self.txtSisiA.grid(row=1, column=1)
        self.txtSisiB = Entry(keliling_frame, borderwidth=1, relief="solid")
        self.txtSisiB.grid(row=2, column=1)
        self.txtSisiC = Entry(keliling_frame, borderwidth=1, relief="solid")
        self.txtSisiC.grid(row=3, column=1)
        #end

        self.txtKeliling = Entry(keliling_frame,font=("Helvetica", 10, "bold"))
        self.txtKeliling.grid(row=5, column=0, columnspan=2,sticky='ew')

        Button(keliling_frame, text="Hitung", command= self.result_keliling, bg="#54B435", fg="white", font=("Helvetica", 10, "bold")).grid(row=4, column=0, columnspan=2,sticky='ew', pady=(10,0))

        luas_frame = Frame(self)
        luas_frame.grid(row=1, column=1, padx=30, sticky='n')

        Label(luas_frame, text="Menghitung Luas", font=subTitleFont()).grid(row=0, column=0,columnspan=2, sticky='n', pady=10)

        #todo
        Label(luas_frame, text= "Alas : ").grid(row=1, column=0)
        Label(luas_frame, text="Tinggi : ").grid(row=2, column=0)

        self.txtAlas = Entry(luas_frame, borderwidth=1, relief="solid")
        self.txtAlas.grid(row=1, column=1)
        self.txtTinggi = Entry(luas_frame, borderwidth=1, relief="solid")
        self.txtTinggi.grid(row=2, column=1)
        #end

        self.txtLuas = Entry(luas_frame,font=("Helvetica", 10, "bold"))
        self.txtLuas.grid(row=4, column=0, columnspan=2,sticky='ew')

        Button(luas_frame, text="Hitung", command= self.result_luas, bg="#54B435", fg="white", font=("Helvetica", 10, "bold")).grid(row=3, column=0, columnspan=2,sticky='ew',pady=(31,0))

        ext_btn = Button(self, text="Kembali", command=lambda: master.main_page(), bg="#E64848", fg="white", font=("Helvetica", 10, "bold"))
        ext_btn.grid(row=2, column=0,columnspan=2, sticky='n', pady=30)

    def result_keliling(self):
            self.txtKeliling.delete(0, END)
            a = float(self.txtSisiA.get())
            b = float(self.txtSisiB.get())
            c = float(self.txtSisiC.get())
            keliling = a+b+c
            self.txtKeliling.insert(0, f"Keliling = {keliling}")

    def result_luas(self):
            self.txtLuas.delete(0, END)
            alas = float(self.txtAlas.get())
            tinggi = float(self.txtTinggi.get())
            luas = 0.5*alas*tinggi
            self.txtLuas.insert(0, f"Luas = {luas}")

class BelahKetupatFrame(Frame):
    def __init__(self, master):
        super().__init__(master, bd=50)
        label = Label(self, text= "Halaman Belah Ketupat",font=titleFont())
        label.grid(row=0, column=0,columnspan=2, sticky='n', pady=30)

        keliling_frame = Frame(self)
        keliling_frame.grid(row=1, column=0, padx=30, sticky='n')

        Label(keliling_frame, text="Menghitung Keliling", font=subTitleFont()).grid(row=0, column=0,columnspan=2, sticky='n', pady=10)

        #todo
        Label(keliling_frame, text= "Sisi A: ").grid(row=1, column=0)
        Label(keliling_frame, text="Sisi B: ").grid(row=2, column=0)
        Label(keliling_frame, text= "Sisi C: ").grid(row=3, column=0)
        Label(keliling_frame, text="Sisi D: ").grid(row=4, column=0)

        self.txtSisiA = Entry(keliling_frame, borderwidth=1, relief="solid")
        self.txtSisiA.grid(row=1, column=1)
        self.txtSisiB = Entry(keliling_frame, borderwidth=1, relief="solid")
        self.txtSisiB.grid(row=2, column=1)
        self.txtSisiC = Entry(keliling_frame, borderwidth=1, relief="solid")
        self.txtSisiC.grid(row=3, column=1)
        self.txtSisiD = Entry(keliling_frame, borderwidth=1, relief="solid")
        self.txtSisiD.grid(row=4, column=1)
        #end

        self.txtKeliling = Entry(keliling_frame,font=("Helvetica", 10, "bold"))
        self.txtKeliling.grid(row=6, column=0, columnspan=2,sticky='ew')

        Button(keliling_frame, text="Hitung", command= self.result_keliling, bg="#54B435", fg="white", font=("Helvetica", 10, "bold")).grid(row=5, column=0, columnspan=2,sticky='ew', pady=(10,0))

        luas_frame = Frame(self)
        luas_frame.grid(row=1, column=1, padx=30, sticky='n')

        Label(luas_frame, text="Menghitung Luas", font=subTitleFont()).grid(row=0, column=0,columnspan=2, sticky='n', pady=10)

        #todo
        Label(luas_frame, text="Diagonal 1 : ").grid(row=1, column=0)
        Label(luas_frame, text="Diagonal 2 : ").grid(row=2, column=0)

        self.txtDiagonal1 = Entry(luas_frame, borderwidth=1, relief="solid")
        self.txtDiagonal1.grid(row=1, column=1)
        self.txtDiagonal2 = Entry(luas_frame, borderwidth=1, relief="solid")
        self.txtDiagonal2.grid(row=2, column=1)
        #end

        self.txtLuas = Entry(luas_frame,font=("Helvetica", 10, "bold"))
        self.txtLuas.grid(row=4, column=0, columnspan=2,sticky='ew')

        Button(luas_frame, text="Hitung", command= self.result_luas, bg="#54B435", fg="white", font=("Helvetica", 10, "bold")).grid(row=3, column=0, columnspan=2,sticky='ew',pady=(53,0))

        ext_btn = Button(self, text="Kembali", command=lambda: master.main_page(), bg="#E64848", fg="white", font=("Helvetica", 10, "bold"))
        ext_btn.grid(row=2, column=0,columnspan=2, sticky='n', pady=30)

    def result_keliling(self):
            self.txtKeliling.delete(0, END)
            a = float(self.txtSisiA.get())
            b = float(self.txtSisiB.get())
            c = float(self.txtSisiC.get())
            d = float(self.txtSisiD.get())
            keliling = a+b+c+d
            self.txtKeliling.insert(0, f"Keliling = {keliling}")

    def result_luas(self):
            self.txtLuas.delete(0, END)
            d1 = float(self.txtDiagonal1.get())
            d2 = float(self.txtDiagonal2.get())
            luas = 0.5*d1*d2
            self.txtLuas.insert(0, f"Luas = {luas}")

class LayangLayangFrame(Frame):
    def __init__(self, master):
        super().__init__(master, bd=50)
        label = Label(self, text= "Halaman Layang-Layang",font=titleFont())
        label.grid(row=0, column=0,columnspan=2, sticky='n', pady=30)

        keliling_frame = Frame(self)
        keliling_frame.grid(row=1, column=0, padx=30, sticky='n')

        Label(keliling_frame, text="Menghitung Keliling", font=subTitleFont()).grid(row=0, column=0,columnspan=2, sticky='n', pady=10)

        #todo
        Label(keliling_frame, text= "Sisi A: ").grid(row=1, column=0)
        Label(keliling_frame, text="Sisi B: ").grid(row=2, column=0)
        Label(keliling_frame, text= "Sisi C: ").grid(row=3, column=0)
        Label(keliling_frame, text="Sisi D: ").grid(row=4, column=0)

        self.txtSisiA = Entry(keliling_frame, borderwidth=1, relief="solid")
        self.txtSisiA.grid(row=1, column=1)
        self.txtSisiB = Entry(keliling_frame, borderwidth=1, relief="solid")
        self.txtSisiB.grid(row=2, column=1)
        self.txtSisiC = Entry(keliling_frame, borderwidth=1, relief="solid")
        self.txtSisiC.grid(row=3, column=1)
        self.txtSisiD = Entry(keliling_frame, borderwidth=1, relief="solid")
        self.txtSisiD.grid(row=4, column=1)
        #end

        self.txtKeliling = Entry(keliling_frame,font=("Helvetica", 10, "bold"))
        self.txtKeliling.grid(row=6, column=0, columnspan=2,sticky='ew')

        Button(keliling_frame, text="Hitung", command= self.result_keliling, bg="#54B435", fg="white", font=("Helvetica", 10, "bold")).grid(row=5, column=0, columnspan=2,sticky='ew', pady=(10,0))

        luas_frame = Frame(self)
        luas_frame.grid(row=1, column=1, padx=30, sticky='n')

        Label(luas_frame, text="Menghitung Luas", font=subTitleFont()).grid(row=0, column=0,columnspan=2, sticky='n', pady=10)

        #todo
        Label(luas_frame, text="Diagonal 1 : ").grid(row=1, column=0)
        Label(luas_frame, text="Diagonal 2 : ").grid(row=2, column=0)

        self.txtDiagonal1 = Entry(luas_frame, borderwidth=1, relief="solid")
        self.txtDiagonal1.grid(row=1, column=1)
        self.txtDiagonal2 = Entry(luas_frame, borderwidth=1, relief="solid")
        self.txtDiagonal2.grid(row=2, column=1)
        #end

        self.txtLuas = Entry(luas_frame,font=("Helvetica", 10, "bold"))
        self.txtLuas.grid(row=4, column=0, columnspan=2,sticky='ew')

        Button(luas_frame, text="Hitung", command= self.result_luas, bg="#54B435", fg="white", font=("Helvetica", 10, "bold")).grid(row=3, column=0, columnspan=2,sticky='ew',pady=(53,0))

        ext_btn = Button(self, text="Kembali", command=lambda: master.main_page(), bg="#E64848", fg="white", font=("Helvetica", 10, "bold"))
        ext_btn.grid(row=2, column=0,columnspan=2, sticky='n', pady=30)

    def result_keliling(self):
            self.txtKeliling.delete(0, END)
            a = float(self.txtSisiA.get())
            b = float(self.txtSisiB.get())
            c = float(self.txtSisiC.get())
            d = float(self.txtSisiD.get())
            keliling = a+b+c+d
            self.txtKeliling.insert(0, f"Keliling = {keliling}")

    def result_luas(self):
            self.txtLuas.delete(0, END)
            d1 = float(self.txtDiagonal1.get())
            d2 = float(self.txtDiagonal2.get())
            luas = 0.5*d1*d2
            self.txtLuas.insert(0, f"Luas = {luas}")  

class TrapesiumFrame(Frame):
    def __init__(self, master):
        super().__init__(master, bd=50)
        label = Label(self, text= "Halaman Trapesium",font=titleFont())
        label.grid(row=0, column=0,columnspan=2, sticky='n', pady=30)

        keliling_frame = Frame(self)
        keliling_frame.grid(row=1, column=0, padx=30, sticky='n')

        Label(keliling_frame, text="Menghitung Keliling", font=subTitleFont()).grid(row=0, column=0,columnspan=2, sticky='n', pady=10)

        #todo
        Label(keliling_frame, text= "Sisi A: ").grid(row=1, column=0)
        Label(keliling_frame, text="Sisi B: ").grid(row=2, column=0)
        Label(keliling_frame, text= "Sisi C: ").grid(row=3, column=0)
        Label(keliling_frame, text="Sisi D: ").grid(row=4, column=0)

        self.txtSisiA = Entry(keliling_frame, borderwidth=1, relief="solid")
        self.txtSisiA.grid(row=1, column=1)
        self.txtSisiB = Entry(keliling_frame, borderwidth=1, relief="solid")
        self.txtSisiB.grid(row=2, column=1)
        self.txtSisiC = Entry(keliling_frame, borderwidth=1, relief="solid")
        self.txtSisiC.grid(row=3, column=1)
        self.txtSisiD = Entry(keliling_frame, borderwidth=1, relief="solid")
        self.txtSisiD.grid(row=4, column=1)
        #end

        self.txtKeliling = Entry(keliling_frame,font=("Helvetica", 10, "bold"))
        self.txtKeliling.grid(row=6, column=0, columnspan=2,sticky='ew')

        Button(keliling_frame, text="Hitung", command= self.result_keliling, bg="#54B435", fg="white", font=("Helvetica", 10, "bold")).grid(row=5, column=0, columnspan=2,sticky='ew', pady=(10,0))

        luas_frame = Frame(self)
        luas_frame.grid(row=1, column=1, padx=30, sticky='n')

        Label(luas_frame, text="Menghitung Luas", font=subTitleFont()).grid(row=0, column=0,columnspan=2, sticky='n', pady=10)

        #todo
        Label(luas_frame, text= "Sisi Sejajar A: ").grid(row=1, column=0)
        Label(luas_frame, text="Sisi Sejajar B: ").grid(row=2, column=0)
        Label(luas_frame, text="Tinggi: ").grid(row=3, column=0)

        self.txtSejajarA = Entry(luas_frame, borderwidth=1, relief="solid")
        self.txtSejajarA.grid(row=1, column=1)
        self.txtSejajarB = Entry(luas_frame, borderwidth=1, relief="solid")
        self.txtSejajarB.grid(row=2, column=1)
        self.txtTinggi = Entry(luas_frame, borderwidth=1, relief="solid")
        self.txtTinggi.grid(row=3, column=1)
        #end

        self.txtLuas = Entry(luas_frame,font=("Helvetica", 10, "bold"))
        self.txtLuas.grid(row=5, column=0, columnspan=2,sticky='ew')

        Button(luas_frame, text="Hitung", command= self.result_luas, bg="#54B435", fg="white", font=("Helvetica", 10, "bold")).grid(row=4, column=0, columnspan=2,sticky='ew',pady=(31,0))

        ext_btn = Button(self, text="Kembali", command=lambda: master.main_page(), bg="#E64848", fg="white", font=("Helvetica", 10, "bold"))
        ext_btn.grid(row=2, column=0,columnspan=2, sticky='n', pady=30)

    def result_keliling(self):
            self.txtKeliling.delete(0, END)
            a = float(self.txtSisiA.get())
            b = float(self.txtSisiB.get())
            c = float(self.txtSisiC.get())
            d = float(self.txtSisiD.get())
            keliling = a+b+c+d
            self.txtKeliling.insert(0, f"Keliling = {keliling}")

    def result_luas(self):
            self.txtLuas.delete(0, END)
            a = float(self.txtSejajarA.get())
            b = float(self.txtSejajarB.get())
            tinggi = float(self.txtTinggi.get())
            luas = 0.5*(a+b)*tinggi
            self.txtLuas.insert(0, f"Luas = {luas}")   

class LingkaranFrame(Frame):
    def __init__(self, master):
        super().__init__(master, bd=50)
        label = Label(self, text= "Halaman Lingkaran",font=titleFont())
        label.grid(row=0, column=0,columnspan=2, sticky='n', pady=30)

        keliling_frame = Frame(self)
        keliling_frame.grid(row=1, column=0, padx=30, sticky='n')

        Label(keliling_frame, text="Menghitung Keliling", font=subTitleFont()).grid(row=0, column=0,columnspan=2, sticky='n', pady=10)

        #todo
        Label(keliling_frame, text= "Jari-jari: ").grid(row=1, column=0)

        self.txtJarijari1 = Entry(keliling_frame, borderwidth=1, relief="solid")
        self.txtJarijari1.grid(row=1, column=1)
        #end

        self.txtKeliling = Entry(keliling_frame,font=("Helvetica", 10, "bold"))
        self.txtKeliling.grid(row=3, column=0, columnspan=2,sticky='ew')

        Button(keliling_frame, text="Hitung", command= self.result_keliling, bg="#54B435", fg="white", font=("Helvetica", 10, "bold")).grid(row=2, column=0, columnspan=2,sticky='ew', pady=(10,0))

        luas_frame = Frame(self)
        luas_frame.grid(row=1, column=1, padx=30, sticky='n')

        Label(luas_frame, text="Menghitung Luas", font=subTitleFont()).grid(row=0, column=0,columnspan=2, sticky='n', pady=10)

        #todo
        Label(luas_frame, text= "Jari-jari: ").grid(row=1, column=0)

        self.txtJarijari2 = Entry(luas_frame, borderwidth=1, relief="solid")
        self.txtJarijari2.grid(row=1, column=1)
        #end

        self.txtLuas = Entry(luas_frame,font=("Helvetica", 10, "bold"))
        self.txtLuas.grid(row=3, column=0, columnspan=2,sticky='ew')

        Button(luas_frame, text="Hitung", command= self.result_luas, bg="#54B435", fg="white", font=("Helvetica", 10, "bold")).grid(row=2, column=0, columnspan=2,sticky='ew',pady=(10,0))

        ext_btn = Button(self, text="Kembali", command=lambda: master.main_page(), bg="#E64848", fg="white", font=("Helvetica", 10, "bold"))
        ext_btn.grid(row=2, column=0,columnspan=2, sticky='n', pady=30)

    def result_keliling(self):
            self.txtKeliling.delete(0, END)
            r = float(self.txtJarijari1.get())
            keliling = 2*3.14*r
            self.txtKeliling.insert(0, f"Keliling = {keliling}")

    def result_luas(self):
            self.txtLuas.delete(0, END)
            r = float(self.txtJarijari2.get())
            luas = 3.14*r*r
            self.txtLuas.insert(0, f"Luas = {luas}")                



class Parent(Tk):
    def __init__(self):
        super().__init__()
        self.title("Bangun Datar")
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

    pageNames = [PersegiFrame, PersegiPanjangFrame,JajarGenjangFrame, SegitigaFrame, BelahKetupatFrame, LayangLayangFrame, TrapesiumFrame, LingkaranFrame]
            
class MainPage(Frame):
    def __init__(self, master):
        super().__init__(master, bd=30 )
        label = Label(self, text= "Pilih bangun datar yang ingin anda hitung luas atau kelilingnya", font=titleFont())
        label.pack()

        buttons = [
            ("Persegi", 0, 0), ("Persegi Panjang",0,1),
            ("Jajar Genjang",1,0), ("Segitiga",1,1),
            ("Belah Ketupat",2,0), ("Layang-Layang",2,1),
            ("Trapesium",3,0), ("Lingkaran",3,1)
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