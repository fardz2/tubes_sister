from xmlrpc.client import ServerProxy
import datetime


class AntreanClient:
    def __init__(self, is_admin=False):
        self.server = ServerProxy("http://localhost:8000")
        self.is_admin = is_admin

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

    def daftar_antrean(self):
        antrean_data = self.server.daftar_antrean()
        for nomor_antrean, antrean_info in antrean_data.items():
            print(f"Nomor Antrean: {nomor_antrean}")
            print(f"Nama: {antrean_info['nama']}")
            print(f"Tanggal Lahir: {antrean_info['tanggal_lahir']}")
            print(f"Klinik: {antrean_info['klinik']}")
            print(f"Waktu Antrean: {antrean_info['waktu_antrean']}")
            print()

    def hapus_antrean(self, nomor_antrean):
        try:
            result = self.server.hapus_antrean(nomor_antrean)
            if result:
                print(f"Antrean {nomor_antrean} berhasil dihapus.")
            else:
                print(f"Antrean {nomor_antrean} tidak ditemukan.")
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    role = input("Masukkan peran Anda (admin/client): ").lower()

    if role == "admin":
        password = input("Masukkan kata sandi admin: ")
        if password != "adminpassword":
            print("Kata sandi admin salah. Keluar.")
            exit()

        client = AntreanClient(is_admin=True)
    elif role == "client":
        client = AntreanClient()
    else:
        print("Peran tidak valid. Keluar.")
        exit()

    while True:
        print("\nMenu:")
        print("1. Registrasi Antrean")
        print("2. Daftar Klinik")
        print("3. Daftar Antrean")
        if client.is_admin:
            print("4. Hapus Antrean (Admin)")
        print("5. Keluar")

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
            client.daftar_antrean()
        elif client.is_admin and choice == "4":
            nomor_antrean = input("Masukkan nomor antrean yang akan dihapus: ")
            client.hapus_antrean(nomor_antrean)
        elif choice == "5":
            break
        else:
            print("Pilihan tidak valid. Silakan pilih lagi.")
