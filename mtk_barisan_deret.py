# Statis
# Nomor 1
i = 13
n = 17
result = 0
while i <= n:
    f = eval('5 * i + 2')
    result += f
    i += 1
print('Jawaban Nomor 1 = ', result)

# Nomor 2
i = 5
n = 10
result = 0
while i <= n:
    f = eval('i**2 + 2*i - 1')
    result += f
    i += 1
print('Jawaban Nomor 2 = ',result)

# Nomor 3
i = 4
n = 8
result = 1
while i <= n:
    f = eval('i - 3')
    result *= f
    i += 1
print('Jawaban Nomor 3 = ', result)

# Dinamis
while True:
    print('Menghitung Baris dan Deret')
    print('''==========
    1. Sigma (5i +2)
    2. Sigma (i^2 + 2i - 1)
    3. Pi (i - 3)
=========''')
    pil = input('Pilih (nomor) : ')
    print('==========')
    result = 0
    i = int(input('Masukkan Bilangan Awal : '))
    n = int(input('Masukkan Bilangan Batas : '))
    while i <= n:
        if pil == '1':
            f = eval('5 * i + 2')
        elif pil == '2':
            f = eval('i**2 + 2*i - 1')
        elif pil == '3':
            f = eval('i - 3')
            result = 1
            result *= f
            continue
        else :
            print('Pilihan Tidak Ditemukan')
            continue
        result += f