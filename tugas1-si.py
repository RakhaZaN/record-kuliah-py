# Fitur 1 | Pendaftaran Anggota
print('Fitur Pendaftaran Anggota')
print()

nama = input('Masukkan Nama : ')
tanggal_lahir = input('Masukkan Tanggal Lahir (dd-mm-yyyy) : ')
umur = 2021 - eval(tanggal_lahir.split('-')[2])
if umur < 17:
    print('Umur Belum Mencukupi')
else :
    penghasilan = eval(input('Penghasilan perbulan  : '))
    if penghasilan < 5000000:
        level = 'Silver'
    elif penghasilan >= 5000000 and penghasilan < 10000000:
        level = 'Gold'
    else :
        level = 'Diamond'
    while True:
        email = input('Masukkan Email : ')
        if '@' not in email or '.com' not in email:
            print('Invalid Email')
        else:
            break
    while True:
        spesialChar = ['!', '@', '#', '$']
        pas = input('Masukkan Password : ')
        if len(pas) < 8:
            print('Password minimal 8 karakter')
            continue
        if not any(char.isupper() for char in pas):
            print('Harus mengandung huruf kapital minimal 1')
            continue
        if not any(char.islower() for char in pas):
            print('Harus mengandung huruf kecil minimal 1')
            continue
        if not any(char.isdigit() for char in pas):
            print('Harus mengandung angka minimal 1')
            continue
        if not any(char in spesialChar for char in pas):
            print('Harus mengandung symbol (!@#$) minimal 1')
            continue
        break
    while True:
        copas = input('Konfirmasi Password : ')
        if copas != pas:
            print('Konfirmasi password tidak sesuai')
        else:
            break
    print()
    print('Pendaftaran Berhasil')
    print(f'''Nama : {nama}
Email : {email}
Level : {level}''')

print()
print('-' * 20)
print()

# Fitur 2 | Belanja
print('Fitur Belanja')
print()

cart = [[],[]]
while True:
    namaProduk = input('Masukkan nama produk yang akan dibeli atau X untuk selesai : ')
    if namaProduk.upper() == 'X':
        break
    hargaProduk = int(input('Masukkan harga produk : '))
    # Memasukkan barang kedalam list
    cart[0].append(namaProduk)
    cart[1].append(hargaProduk)
    print(cart)
    print(f"Berhasil menambahkan {namaProduk} dengan harga {hargaProduk}")

print()
jmlProduk = len(cart[0])
total = sum(cart[1])
if len(cart[0]) == 0:
    print('Terimakasih. Sampai Jumpa!')
else:
    print('Total produk yang dibeli : ', jmlProduk)
    print('Total harga produk : ', total)
    print()

    isAnggota = input('Apakah Anda seorang anggota? (Y/T) : ').upper()
    if isAnggota == 'Y':
        while True:
            aEmail = input('Masukkan email : ')
            if '@' not in aEmail or '.com' not in aEmail:
                print('Invalid Email')
            else:
                break
        
        while True:
            spesialChar = ['!', '@', '#', '$']
            pas = input('Masukkan password : ')
            if len(pas) < 8:
                print('Password minimal 8 karakter')
                continue
            if not any(char.isupper() for char in pas):
                print('Harus mengandung huruf kapital minimal 1')
                continue
            if not any(char.islower() for char in pas):
                print('Harus mengandung huruf kecil minimal 1')
                continue
            if not any(char.isdigit() for char in pas):
                print('Harus mengandung angka minimal 1')
                continue
            if not any(char in spesialChar for char in pas):
                print('Harus mengandung symbol (!@#$) minimal 1')
                continue
            break
        
        while True:
            aLevel = input('Masukkan level kepesertaan Anda (Silver | Gold | Diamond) : ').capitalize()
            if aLevel == 'Silver':
                total -= 5/100 * total if jmlProduk < 5 else 10/100 * total
                persen = '5%' if jmlProduk < 5 else '10%'
            elif aLevel == 'Gold':
                total -= 10/100 * total if jmlProduk < 5 else 15/100 * total
                persen = '10%' if jmlProduk < 5 else '15%'
            elif aLevel == 'Diamond':
                total -= 15/100 * total if jmlProduk < 5 else 20/100 * total
                persen = '15%' if jmlProduk < 5 else '20%'
            else:
                print('Level tidak valid')
                continue
            print('Selamat Anda mendapatkan discount sebesar ', persen)
            break
        
    print('Total harga yang harus dibayar : ', total)
    print('Terimakasih telah berbelanja di NFElectronics')
