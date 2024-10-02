import random
# Ini kelas buat proses data inputnya ya - RCQ
class PermainanBatuGuntingKertas:
    
    def pilihan_komputer(self):
        pilihan = ["batu", "gunting", "kertas"]
        return random.choice(pilihan)

    def tampilkan_hasil(self, pemain, komputer, hasil):
        print(f"Pemain memilih: {pemain}")
        print(f"Komputer memilih: {komputer}")
        print(f"Hasil: {hasil}")
    
    def perkenalan(self):
        print("Selamat datang di permainan Batu Gunting Kertas!\n")

    def tentukan_pemenang(self, pemain, komputer):
        if pemain == komputer:
            return "Seri!"
        elif (pemain == "batu" and komputer == "gunting") or \
             (pemain == "gunting" and komputer == "kertas") or \
             (pemain == "kertas" and komputer == "batu"):
            return "Kamu menang!"
        else:
            return "Komputer menang!"

#Fungsi buat jalanin gamenya - Lionel
def main():
    game = PermainanBatuGuntingKertas()
    game.perkenalan()

    while True:
        pemain = input("\nPilih batu, gunting, atau kertas (atau ketik 'keluar' untuk berhenti): ").lower()

        if pemain == "keluar":
            print("terima kasih telah bermain")
            break
        # tambahin error message dong - RCQ
        
        # Method dengan return type dan tanpa parameter
        komputer = game.pilihan_komputer()
        
        # Function dengan parameter dan return type
        hasil = game.tentukan_pemenang(pemain, komputer)


