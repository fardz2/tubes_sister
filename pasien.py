from xmlrpc.client import ServerProxy
import datetime


class AntreanClient:
    def __init__(self):
        self.server = ServerProxy("http://localhost:8000")
        self.nomor_rekam = None

    def registrasi(self, nomor_rekam, nama, tanggal_lahir, klinik):
        self.nomor_rekam = nomor_rekam
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
        
        # debugging
        print("Received data from server:", antrean_data)
        
        if antrean_data:
            antrean_found = False
            for nomor_antrean, antrean_info in antrean_data.items():
                if self.nomor_rekam is not None and antrean_info.get("nomor_rekam") == self.nomor_rekam:
                    print(f"Nomor Antrean Anda: {nomor_antrean}")
                    print(f"Waktu Antrean: {antrean_info['waktu_antrean']}")
                    print()
                    antrean_found = True
                    break

            if not antrean_found:
                print(f"{'Anda tidak memiliki antrean' if self.nomor_rekam is not None else 'Antrian kosong'} untuk klinik {klinik}")
        else:
            print(f"Antrian kosong untuk klinik {klinik}")


if __name__ == "__main__":
    client = AntreanClient()

    while True:
        print("\nMenu Pasien:")
        print("1. Registrasi Antrean")
        print("2. Daftar Klinik")
        print("3. Daftar Antrean")
        print("4. keluar")

        choice = input("Pilih menu (1/2/3/4): ")

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
