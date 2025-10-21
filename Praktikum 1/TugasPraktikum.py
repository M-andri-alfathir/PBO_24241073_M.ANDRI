# Kelas PersegiPanjang menggunakan konsep OOP

class PersegiPanjang:
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar

    def hitung_luas(self):
        return self.panjang * self.lebar

    def hitung_keliling(self):
        return 2 * (self.panjang + self.lebar)


# --- Program Utama ---
print("=== Program Menghitung Luas dan Keliling Persegi Panjang ===")
# Input dari pengguna
panjang = float(input("Masukkan panjang: "))
lebar = float(input("Masukkan lebar: "))

 # Membuat objek dari kelas PersegiPanjang
persegi_panjang = PersegiPanjang(panjang, lebar)

 # Menampilkan hasil
print("\nHasil Perhitungan:")
print(f"Luas Persegi Panjang     = {persegi_panjang.hitung_luas()}")
print(f"Keliling Persegi Panjang = {persegi_panjang.hitung_keliling()}")