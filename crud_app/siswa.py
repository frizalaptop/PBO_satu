from db import Database

class Siswa:
    def __init__(self):
        self._nis = None
        self._nama = None
        self._kelas = None
        self._gender = None

    @property
    def nis(self):
        return self._nis

    @property
    def nama(self):
        return self._nama

    @property
    def kelas(self):
        return self._kelas

    @property
    def gender(self):
        return self._gender
    
    @nis.setter
    def nis(self, new_nis):
        self._nis = new_nis

    @nama.setter
    def nama(self, new_nama):
        self._nama = new_nama

    @kelas.setter
    def kelas(self, new_kelas):
        self._kelas = new_kelas

    @gender.setter
    def gender(self, new_gender):
        self._gender = new_gender

    def tambah_siswa(self):
        db = Database()
        db.connect()
        db.insert_siswa(self._nis, self._nama, self._kelas, self._gender)
        db.disconnect()

    def lihat_siswa(self):
        db = Database()
        db.connect()
        return db.read_siswa()

    def perbarui_siswa(self):
        db = Database()
        db.connect()
        db.update_siswa( self._nama, self._kelas, self._gender, self._nis)
        db.disconnect()

    def hapus_siswa(self):
        db = Database()
        db.connect()
        db.delete_siswa(self._nis)
        db.disconnect()
