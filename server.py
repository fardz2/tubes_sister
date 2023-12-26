# Import modul yang dibutuhkan
from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
import datetime


# Definisikan kelas AntreanServer
class AntreanServer:
    def __init__(self):
        # Inisialisasi daftar klinik dan antrean pada klinik
        self.klinik = {"A": [], "B": []}
        self.antrean_klinik = {"A": {}, "B": {}}

    # Metode untuk registrasi pasien ke dalam antrean suatu klinik
    def registrasi(self, nomor_rekam, nama, tanggal_lahir, klinik):
        # Periksa apakah klinik yang dimasukkan valid
        if klinik not in self.klinik:
            return "Klinik tidak valid."

        # Dapatkan nomor antrean berikutnya untuk klinik tertentu
        nomor_antrean = len(self.klinik[klinik]) + 1
        self.klinik[klinik].append(nomor_antrean)

        # Hitung waktu antrean, set dalam format yang sesuai, dan simpan informasi antrean
        waktu_antrean = datetime.datetime.now() + datetime.timedelta(minutes=30)
        format_jam = waktu_antrean.strftime("%m/%d/%Y, %H:%M:%S")

        nomor_antrean_str = str(nomor_antrean)
        self.antrean_klinik[klinik][nomor_antrean_str] = {
            "nomor_rekam": nomor_rekam,
            "nama": nama,
            "tanggal_lahir": tanggal_lahir,
            "klinik": klinik,
            "waktu_antrean": format_jam,
        }

        # Kembalikan nomor antrean dan waktu antrean kepada pengguna
        return nomor_antrean_str, format_jam

    # Metode untuk mendapatkan daftar klinik yang tersedia
    def daftar_klinik(self):
        return list(self.klinik.keys())

    # Metode untuk mendapatkan daftar antrean pada suatu klinik
    def daftar_antrean_klinik(self, klinik):
        return self.antrean_klinik.get(klinik, {})

    # Metode untuk menghapus antrean dari suatu klinik
    def hapus_antrean(self, klinik, nomor_antrean):
        try:
            nomor_antrean_str = str(nomor_antrean)
            # Periksa apakah antrean dengan nomor tertentu ada pada klinik
            if (
                klinik in self.antrean_klinik
                and nomor_antrean_str in self.antrean_klinik[klinik]
            ):
                nomor_antrean_int = int(nomor_antrean)

                # Hapus nomor antrean dari klinik
                self.klinik[klinik].remove(nomor_antrean_int)

                # Hapus informasi antrean dari daftar antrean
                del self.antrean_klinik[klinik][nomor_antrean_str]

                # Berhasil menghapus antrean
                return True
            else:
                # Gagal menghapus antrean karena tidak ditemukan
                return False
        except Exception as e:
            # Menangani kesalahan jika terjadi
            print(f"Error: {e}")
            return False


# Jalankan server jika dijalankan sebagai skrip utama
if __name__ == "__main__":
    # Inisialisasi objek AntreanServer
    server = SimpleXMLRPCServer(("localhost", 8000), allow_none=True)
    server.register_instance(AntreanServer())
    print("Server ready on localhost:8000. Press Ctrl+C to exit.")
    # Jalankan server secara terus-menerus
    server.serve_forever()
