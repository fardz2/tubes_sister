from xmlrpc.client import ServerProxy
import datetime


class AntreanClient:
    def __init__(self):
        self.server = ServerProxy("http://localhost:8000")

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

    def hapus_antrean(self):
        try:
            # Meminta input klinik
            klinik = input("Masukkan klinik: ")
            # Menampilkan daftar antrean untuk klinik tertentu
            self.daftar_antrean_klinik(klinik)

            # Meminta input nomor antrean
            nomor_antrean = input("Masukkan nomor antrean yang akan dihapus: ")
            result = self.server.hapus_antrean(klinik, nomor_antrean)

            if result:
                print(f"Antrean {nomor_antrean} di klinik {klinik} berhasil dihapus.")
            else:
                print(f"Antrean {nomor_antrean} di klinik {klinik} tidak ditemukan.")
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    client = AntreanClient()
    while True:
        print("\nMenu Admin:")
        print("1. Daftar Klinik")
        print("2. Daftar Antrean")
        print("3. Hapus Antrean (Admin)")
        print("4. Keluar")

        choice = input("Pilih menu (1/2/3/4): ")

        if choice == "1":
            client.daftar_klinik()
        elif choice == "2":
            klinik = input("Masukkan klinik yang ingin dilihat antreannya: ")
            client.daftar_antrean_klinik(klinik)
        elif choice == "3":
            client.hapus_antrean()
        elif client and choice == "4":
            break
        else:
            print("Pilihan tidak valid. Silakan pilih lagi.")
