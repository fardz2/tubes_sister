# Import modul yang dibutuhkan
from xmlrpc.client import ServerProxy


# Definisikan kelas AntreanPasien
class AntreanPasien:
    def __init__(self):
        # Inisialisasi objek server proxy untuk berkomunikasi dengan server XML-RPC
        self.server = ServerProxy("http://localhost:8000")
        # Inisialisasi nomor rekam pasien sebagai atribut kelas
        self.nomor_rekam = None

    # Metode untuk registrasi pasien ke dalam antrean
    def registrasi(self, nomor_rekam, nama, tanggal_lahir, klinik):
        # Panggil metode registrasi dari server dan dapatkan nomor antrean dan waktu antrean
        nomor_antrean, waktu_antrean = self.server.registrasi(
            nomor_rekam, nama, tanggal_lahir, klinik
        )
        # Tampilkan informasi registrasi kepada pengguna
        print(f"Registrasi berhasil. Nomor Antrean: {nomor_antrean}")
        print(f"Perkiraan waktu antrean: {waktu_antrean}")

    # Metode untuk mendapatkan daftar klinik yang tersedia
    def daftar_klinik(self):
        # Panggil metode daftar_klinik dari server dan tampilkan hasilnya
        klinik_list = self.server.daftar_klinik()
        print("Daftar Klinik yang Buka:")
        for klinik in klinik_list:
            print(f"- {klinik}")

    # Metode untuk mendapatkan daftar antrean pada suatu klinik
    def daftar_antrean_klinik(self, klinik):
        # Panggil metode daftar_antrean_klinik dari server dan dapatkan data antrean
        antrean_data = self.server.daftar_antrean_klinik(klinik)
        if antrean_data:
            antrean_found = False
            # Iterasi antara nomor antrean dan informasi antrean pada klinik
            for nomor_antrean, antrean_info in antrean_data.items():
                # Periksa apakah nomor rekam pasien sesuai dengan antrean yang ditemukan
                if (
                    self.nomor_rekam is not None
                    and antrean_info.get("nomor_rekam") == self.nomor_rekam
                ):
                    print(f"Nomor Antrean Anda: {nomor_antrean}")
                    print(f"Waktu Antrean: {antrean_info['waktu_antrean']}")
                    print()
                    antrean_found = True
                    break

            # Tampilkan pesan jika antrean tidak ditemukan
            if not antrean_found:
                print(
                    f"{'Anda tidak memiliki antrean' if self.nomor_rekam is not None else 'Antrean kosong'} untuk klinik {klinik}"
                )
        else:
            # Tampilkan pesan jika antrean kosong untuk klinik tertentu
            print(f"Antrean kosong untuk klinik {klinik}")


# Jalankan program jika dijalankan sebagai skrip utama
if __name__ == "__main__":
    # Inisialisasi objek AntreanPasien
    pasien = AntreanPasien()

    # Loop utama program
    while True:
        # Tampilkan menu pilihan kepada pengguna
        print("\nMenu Pasien:")
        print("1. Registrasi Antrean")
        print("2. Daftar Klinik")
        print("3. Daftar Antrean")
        print("4. Keluar")

        # Terima input pilihan dari pengguna
        choice = input("Pilih menu (1/2/3/4): ")

        # Proses pilihan pengguna
        if choice == "1":
            # Meminta informasi dari pengguna untuk registrasi antrean
            nomor_rekam = input("Masukkan nomor rekam medis: ")
            nama = input("Masukkan nama: ")
            tanggal_lahir = input("Masukkan tanggal lahir (YYYY-MM-DD): ")
            klinik = input("Pilih klinik: ")
            # Panggil metode registrasi dari objek AntreanPasien
            pasien.registrasi(nomor_rekam, nama, tanggal_lahir, klinik)
        elif choice == "2":
            # Panggil metode daftar_klinik dari objek AntreanPasien
            pasien.daftar_klinik()
        elif choice == "3":
            # Meminta informasi dari pengguna untuk melihat antrean suatu klinik
            klinik = input("Masukkan klinik yang ingin dilihat antreannya: ")
            # Panggil metode daftar_antrean_klinik dari objek AntreanPasien
            pasien.daftar_antrean_klinik(klinik)
        elif choice == "4":
            # Keluar dari loop utama jika pilihan adalah 4
            break
        else:
            # Tampilkan pesan jika pilihan tidak valid
            print("Pilihan tidak valid. Silakan pilih lagi.")
