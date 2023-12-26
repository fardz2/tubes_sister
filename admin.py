# Import modul yang dibutuhkan
from xmlrpc.client import ServerProxy


# Definisikan kelas AntreanAdmin
class AntreanAdmin:
    def __init__(self):
        # Inisialisasi objek server proxy untuk berkomunikasi dengan server XML-RPC
        self.server = ServerProxy("http://localhost:8000")

    # Metode untuk menampilkan daftar klinik yang tersedia
    def daftar_klinik(self):
        # Panggil metode daftar_klinik dari server dan tampilkan hasilnya
        klinik_list = self.server.daftar_klinik()
        print("Daftar Klinik yang Buka:")
        for klinik in klinik_list:
            print(f"- {klinik}")

    # Metode untuk menampilkan daftar antrean pada suatu klinik
    def daftar_antrean_klinik(self, klinik):
        # Panggil metode daftar_antrean_klinik dari server dan dapatkan data antrean
        antrean_data = self.server.daftar_antrean_klinik(klinik)
        if not antrean_data:
            print("Antrean kosong untuk klinik", klinik)
        else:
            # Iterasi antara nomor antrean dan informasi antrean pada klinik
            for nomor_antrean, antrean_info in antrean_data.items():
                # Tampilkan informasi antrean
                print(f"Nomor Antrean: {nomor_antrean}")
                print(f"Nama: {antrean_info['nama']}")
                print(f"Tanggal Lahir: {antrean_info['tanggal_lahir']}")
                print(f"Klinik: {antrean_info['klinik']}")
                print(f"Waktu Antrean: {antrean_info['waktu_antrean']}")
                print()

    # Metode untuk menghapus antrean dari suatu klinik
    def hapus_antrean(self):
        try:
            # Meminta input klinik
            klinik = input("Masukkan klinik: ")
            # Menampilkan daftar antrean untuk klinik tertentu
            self.daftar_antrean_klinik(klinik)

            # Meminta input nomor antrean
            nomor_antrean = input("Masukkan nomor antrean yang akan dihapus: ")
            # Memanggil metode hapus_antrean dari server dan mendapatkan hasilnya
            result = self.server.hapus_antrean(klinik, nomor_antrean)

            # Menampilkan hasil penghapusan antrean
            if result:
                print(f"Antrean {nomor_antrean} di klinik {klinik} berhasil dihapus.")
            else:
                print(f"Antrean {nomor_antrean} di klinik {klinik} tidak ditemukan.")
        except Exception as e:
            # Menangani kesalahan jika terjadi
            print(f"Error: {e}")


# Jalankan program jika dijalankan sebagai skrip utama
if __name__ == "__main__":
    # Inisialisasi objek AntreanAdmin
    admin = AntreanAdmin()

    # Loop utama program
    while True:
        # Menampilkan menu pilihan kepada pengguna
        print("\nMenu Admin:")
        print("1. Daftar Klinik")
        print("2. Daftar Antrean")
        print("3. Hapus Antrean (Admin)")
        print("4. Keluar")

        # Menerima input pilihan dari pengguna
        choice = input("Pilih menu (1/2/3/4): ")

        # Proses pilihan pengguna
        if choice == "1":
            # Menampilkan daftar klinik
            admin.daftar_klinik()
        elif choice == "2":
            # Meminta input klinik untuk melihat daftar antrean
            klinik = input("Masukkan klinik yang ingin dilihat antreannya: ")
            # Menampilkan daftar antrean untuk klinik tertentu
            admin.daftar_antrean_klinik(klinik)
        elif choice == "3":
            # Memanggil metode hapus_antrean untuk menghapus antrean
            admin.hapus_antrean()
        elif choice == "4":
            # Keluar dari loop utama jika pilihan adalah 4
            break
        else:
            # Menampilkan pesan jika pilihan tidak valid
            print("Pilihan tidak valid. Silakan pilih lagi.")
