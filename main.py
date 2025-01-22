class Hotel:
    def __init__(self):
        # Kamar hotel dengan informasi nomor kamar, tipe kamar, harga, dan status ketersediaan
        self.kamar = {
            101: {'tipe': 'Single', 'harga': 500000, 'tersedia': True},
            102: {'tipe': 'Double', 'harga': 750000, 'tersedia': True},
            103: {'tipe': 'Suite', 'harga': 1500000, 'tersedia': True},
            104: {'tipe': 'Family', 'harga': 1000000, 'tersedia': True},
        }
        # Menyimpan daftar reservasi
        self.reservasi = []

    def tampilkan_kamar_tersedia(self):
        print("\nKamar yang tersedia:")
        for no_kamar, info in self.kamar.items():
            if info['tersedia']:
                print(f"Kamar {no_kamar} ({info['tipe']}): Rp{info['harga']:,} per malam")

    def buat_reservasi(self):
        print("\n=== Proses Reservasi ===")
        self.tampilkan_kamar_tersedia()

        try:
            no_kamar = int(input("\nMasukkan nomor kamar yang ingin Anda pesan: "))

            if no_kamar not in self.kamar:
                print("Nomor kamar tidak valid!")
                return

            if self.kamar[no_kamar]['tersedia']:
                nama = input("Masukkan nama Anda: ")
                durasi = int(input("Berapa lama Anda akan menginap (dalam malam): "))

                total_biaya = self.kamar[no_kamar]['harga'] * durasi
                self.reservasi.append({'nama': nama, 'no_kamar': no_kamar, 'durasi': durasi, 'total_biaya': total_biaya})

                # Menandai kamar sebagai tidak tersedia
                self.kamar[no_kamar]['tersedia'] = False
                print(f"\nReservasi berhasil!\nNama: {nama}\nKamar: {self.kamar[no_kamar]['tipe']}\nDurasi: {durasi} malam")
                print(f"Total biaya: Rp{total_biaya:,}")
            else:
                print("Maaf, kamar tersebut sudah terisi.")
        except ValueError:
            print("Input tidak valid! Silakan coba lagi.")

    def tampilkan_reservasi(self):
        if not self.reservasi:
            print("\nBelum ada reservasi.")
            return

        print("\nDaftar Reservasi:")
        for idx, res in enumerate(self.reservasi, start=1):
            print(f"{idx}. Nama: {res['nama']}, Kamar: {self.kamar[res['no_kamar']]['tipe']}, Durasi: {res['durasi']} malam, Total Biaya: Rp{res['total_biaya']:,}")

    def batalkan_reservasi(self):
        self.tampilkan_reservasi()
        if not self.reservasi:
            return

        try:
            no_reservasi = int(input("\nMasukkan nomor reservasi yang ingin dibatalkan: "))
            if 1 <= no_reservasi <= len(self.reservasi):
                reservasi_dibatalkan = self.reservasi.pop(no_reservasi - 1)
                self.kamar[reservasi_dibatalkan['no_kamar']]['tersedia'] = True
                print(f"Reservasi atas nama {reservasi_dibatalkan['nama']} telah dibatalkan.")
            else:
                print("Nomor reservasi tidak valid!")
        except ValueError:
            print("Input tidak valid! Silakan coba lagi.")

    def menu(self):
        while True:
            print("\n=== Menu Utama ===")
            print("1. Buat Reservasi")
            print("2. Lihat Daftar Reservasi")
            print("3. Batalkan Reservasi")
            print("4. Keluar")

            pilihan = input("Pilih menu (1/2/3/4): ")

            if pilihan == '1':
                self.buat_reservasi()
            elif pilihan == '2':
                self.tampilkan_reservasi()
            elif pilihan == '3':
                self.batalkan_reservasi()
            elif pilihan == '4':
                print("Terima kasih telah menggunakan Sistem Manajemen Reservasi Hotel.")
                break
            else:
                print("Pilihan tidak valid, coba lagi.")

if __name__ == "__main__":
    hotel = Hotel()
    hotel.menu()
