import mysql.connector

class Database:
    def __init__(self):
        self.host = "localhost"
        self.user = "root"
        self.password = ""
        self.database = "sekolah"
        self.connection = None
        self.cursor = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            self.cursor = self.connection.cursor()
            print(f"Berhasil terhubung ke database {self.database}")
        except mysql.connector.Error as err:
            print(f"Error: {err}")

    def disconnect(self):
        self.cursor.close()
        self.connection.close()
        print("Terputus dari database")

    def insert_siswa(self, nis, nama, kelas, gender):
        insert_query = """
        INSERT INTO siswa (nis, nama, kelas, gender) VALUES (%s, %s, %s, %s)
        """
        data = (nis, nama, kelas, gender)
        self.cursor.execute(insert_query, data)
        self.connection.commit()
        print("Data siswa berhasil ditambahkan")

    def read_siswa(self):
        select_query = "SELECT * FROM siswa"
        self.cursor.execute(select_query)
        results = self.cursor.fetchall()
        return results

    def update_siswa(self, new_nama, new_kelas, new_gender, new_nis):
        update_query = """
        UPDATE siswa SET
        nama = %s, kelas = %s, gender = %s
        WHERE nis = %s
        """
        data = ( new_nama, new_kelas, new_gender, new_nis)
        self.cursor.execute(update_query, data)
        self.connection.commit()

    def delete_siswa(self, siswa_nis):
        delete_query = "DELETE FROM siswa WHERE nis = %s"
        data = (siswa_nis,)
        self.cursor.execute(delete_query, data)
        self.connection.commit()
        print("Data siswa berhasil dihapus")
