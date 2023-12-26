from xmlrpc.client import ServerProxy
import datetime


class AntreanClient:
    def __init__(self):
        self.server = ServerProxy("http://localhost:8000")

    def registrasi(self, nomor_rekam, nama, tanggal_lahir, klinik):
        nomor_antrean, waktu_antrean = self.server.registrasi(
            nomor_rekam, nama, tanggal_lahir, klinik
        )
        print(f"Registrasi berhasil. Nomor Antrean: {nomor_antrean}")
        print(f"Perkiraan waktu antrean: {waktu_antrean}")

    def daftar_klinik(self):
        klinik_list = self.server.daftar_klinik()
        print("Daftar Klinik yang Buka:")
        for klinik in klinik_list:
            print(f"- {klinik}")

    def daftar_antrean_klinik(self, klinik):
        antrean_data = self.server.daftar_antrean_klinik(klinik)
        if not antrean_data:
            print("Antrian kosong untuk klinik", klinik)
        else:
            for nomor_antrean, antrean_info in antrean_data.items():
                print(f"Nomor Antrean: {nomor_antrean}")
                print(f"Nama: {antrean_info['nama']}")
                print(f"Tanggal Lahir: {antrean_info['tanggal_lahir']}")
                print(f"Klinik: {antrean_info['klinik']}")
                print(f"Waktu Antrean: {antrean_info['waktu_antrean']}")
                print()

    def daftar_antrean(self):
        antrean_data = self.server.daftar_antrean()
        if not antrean_data:
            print("Antrian kosong.")
        else:
            for klinik, antrean_klinik in antrean_data.items():
                print(f"Klinik: {klinik}")
                for nomor_antrean, antrean_info in antrean_klinik.items():
                    print(f"Nomor Antrean: {nomor_antrean}")
                    print(f"Nama: {antrean_info['nama']}")
                    print(f"Tanggal Lahir: {antrean_info['tanggal_lahir']}")
                    print(f"Klinik: {antrean_info['klinik']}")
                    print(f"Waktu Antrean: {antrean_info['waktu_antrean']}")
                    print()


if __name__ == "__main__":
    client = AntreanClient()

    while True:
        print("\nMenu Pasien:")
        print("1. Registrasi Antrean")
        print("2. Daftar Klinik")
        print("3. Daftar Antrean")
        print("4. keluar")

        choice = input("Pilih menu (1/2/3/4/5): ")

        if choice == "1":
            nomor_rekam = input("Masukkan nomor rekam medis: ")
            nama = input("Masukkan nama: ")
            tanggal_lahir = input("Masukkan tanggal lahir (YYYY-MM-DD): ")
            klinik = input("Pilih klinik: ")
            client.registrasi(nomor_rekam, nama, tanggal_lahir, klinik)
        elif choice == "2":
            client.daftar_klinik()
        elif choice == "3":
            klinik = input("Masukkan klinik yang ingin dilihat antreannya: ")
            client.daftar_antrean_klinik(klinik)
        elif choice == "4":
            break
        else:
            print("Pilihan tidak valid. Silakan pilih lagi.")
