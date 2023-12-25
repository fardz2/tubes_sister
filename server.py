from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
import datetime


class AntreanServer:
    def __init__(self):
        self.klinik = {"A": [], "B": []}
        self.antrean = dict()

    def registrasi(self, nomor_rekam, nama, tanggal_lahir, klinik):
        if klinik not in self.klinik:
            return "Klinik tidak valid."

        nomor_antrean = len(self.klinik[klinik]) + 1
        self.klinik[klinik].append(nomor_antrean)

        waktu_antrean = datetime.datetime.now() + datetime.timedelta(minutes=30)

        # Mengonversi waktu antrean ke format jam
        format_jam = waktu_antrean.strftime("%m/%d/%Y, %H:%M:%S")

        print("Perkiraan waktu antrean:", format_jam)

        # Konversi nomor antrean ke string sebelum digunakan sebagai kunci
        nomor_antrean_str = str(nomor_antrean)
        self.antrean[nomor_antrean_str] = {
            "nomor_rekam": nomor_rekam,
            "nama": nama,
            "tanggal_lahir": tanggal_lahir,
            "klinik": klinik,
            "waktu_antrean": format_jam,
        }

        return nomor_antrean_str, format_jam

    def daftar_klinik(self):
        return list(self.klinik.keys())

    def daftar_antrean(self):
        return self.antrean

    def daftar_antrean_klinik(self, klinik):
        result = {}
        for nomor_antrean, antrean_info in self.antrean.items():
            if antrean_info["klinik"] == f"Klinik {klinik}":
                result[nomor_antrean] = antrean_info
        return result

    def hapus_antrean(self, nomor_antrean):
        try:
            nomor_antrean_str = str(nomor_antrean)
            if nomor_antrean_str in self.antrean:
                klinik = self.antrean[nomor_antrean_str]["klinik"]
                nomor_antrean_int = int(nomor_antrean)

                # Hapus antrian dari klinik
                self.klinik[klinik].remove(nomor_antrean_int)

                # Perbarui waktu antrean untuk antrian yang tersisa di klinik
                for nomor in self.klinik[klinik]:
                    nomor_str = str(nomor)
                    self.antrean[nomor_str]["waktu_antrean"] = (
                        datetime.datetime.now() + datetime.timedelta(minutes=30)
                    ).strftime("%m/%d/%Y, %H:%M:%S")

                # Hapus antrian dari daftar antrean
                del self.antrean[nomor_antrean_str]

                return True
            else:
                return False
        except Exception as e:
            print(f"Error: {e}")
            return False


if __name__ == "__main__":
    server = SimpleXMLRPCServer(("localhost", 8000), allow_none=True)
    server.register_instance(AntreanServer())
    print("Server ready on localhost:8000. Press Ctrl+C to exit.")
    server.serve_forever()
