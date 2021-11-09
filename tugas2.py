# Rakha Zahran Nurfirmansyah
# 0110221254
# TI 11
# Tugas 2 | Toko Elektronik

print('Selamat Datang Di Toko Online Elektronik')
print('=' * 20)
nama = input('Silahkan masukkan nama Anda : ')

produk = {
    'tv': 2000000,
    'ac': 1500000,
    'kulkas': 1200000,
    'mesin_cuci': 1000000,
    'kipas_angin': 200000
}
disc = 0.05
print("""
List produk yang tersedia
1. TV
2. AC 
3. Kulkas
4. Mesin Cuci
5. Kipas Angin
====================""")
pil = input('Masukkan nomor produk yang ingin dibeli : ')

if pil in ['1', '2', '3', '4', '5']:
    qty = int(input('Masukkan banyak produk : '))
    if pil == '1':
        proPil = 'TV'
        total = qty * produk['tv']
    elif pil == '2':
        proPil = 'AC'
        total = qty * produk['ac']
        disc = 0.1 if qty >= 3 else disc
    elif pil == '3':
        proPil = 'Kulkas'
        total = qty * produk['kulkas']
        disc = 0.2 if qty >= 5 else disc
    elif pil == '4':
        proPil = 'Mesin Cuci'
        total = qty * produk['mesin_cuci']
    elif pil == '5':
        proPil = 'Kipas Angin'
        total = qty * produk['kipas_angin']

    # Print Struk
    ppn = total * 0.1
    disc = total * disc
    totalBayar = total - disc + ppn
    print(f"""====================
Struk Pembayaran
--------------------
Nama Pelanggan \t\t: {nama}
Produk \t\t\t: {proPil}
Jumlah \t\t\t: {qty}
total \t\t\t: {total}
discount \t\t: {int(disc)}
ppn \t\t\t: {int(ppn)}
Total Pembayaran \t: {int(totalBayar)}
===================""")
else:
    print('Produk tidak ditemukan!')
