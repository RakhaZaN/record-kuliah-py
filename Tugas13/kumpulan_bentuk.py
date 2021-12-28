from Lingkaran import *
from SegitigaSiku2 import *
from PersegiPanjang import *

print('Menghitung Luas dan Keliling Bangun Datar')
print('=============== Nilai Statis saat Instansiasi Objek ==============')
lingkaran = Lingkaran('Lingkaran 1', 7)
lingkaran.cetak()

segi3 = Segi3Siku2('Segitiga Siku Siku 1', 10, 5)
segi3.cetak()

perpan = PersegiPanjang('Persegi Panjang 1', 12, 10)
perpan.cetak()

perpan = PersegiPanjang('Persegi Panjang 2', 20, 5)
perpan.cetak()

print('=============== Nilai Input dari User ==============')
while True:
    print("""Menu
    1. Lingkaran
    2. Persegi Panjang
    3. Segitiga Siku-Siku
    0. Keluar
    """)
    pil = input('Masukkan pilihan: ')

    if pil == "0":
        print('==================== Anda telah keluar ====================')
        break

    if pil == "1":
        r = int(input('Masukkan jari-jari (r) : '))
        user_lingkaran = Lingkaran('User Lingkaran', r)
        user_lingkaran.cetak()
    elif pil == "2":
        p = int(input('Masukkan panjang (p) : '))
        l = int(input('Masukkan lebar (l) : '))
        user_perpan = PersegiPanjang('User Persegi Panjang', p, l)
        user_perpan.cetak()
    elif pil == "3":
        a = int(input('Masukkan alas (a) : '))
        t = int(input('Masukkan tinggi (t) : '))
        user_segi3 = Segi3Siku2('User Segitiga Siku Siku', a, t)
        user_segi3.cetak()
    else:
        print('Pilihan tidak ditemukan! \nCoba lagi!!')