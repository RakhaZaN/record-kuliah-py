# Tugas 1
# Nama : Rakha Zahran Nurfirmansyah
# NIM : 0110221254
# Rombel : TI 11

# Mencetak data Slip Gaji
print('SLIP GAJI PT. XYZ')
print('-' * 20)
nama = input('Nama \t\t\t: ')
agama = input('Agama \t\t\t: ').lower()
anak = int(input('Jumlah Anak \t\t: '))
gPokok = int(input('Gaji Pokok \t\t: Rp'))
tJabatan = gPokok * 20/100
if anak == 0:
    tKeluarga = 0
elif anak <= 2:
    tKeluarga = gPokok * 10/100
else:
    tKeluarga = gPokok * 20/100
gKotor = gPokok + tJabatan + tKeluarga
zakat = (0, 0.025)[agama == 'islam' and gKotor >= 6000000] * gKotor
# zakat = gKotor * 2.5/100 if agama == 'islam' and gKotor > 6000000 else 0
gBersih = gKotor - zakat
print('Tunjangan Jabatan \t: Rp', tJabatan)
print('Tunjangan Keluarga \t: Rp', tKeluarga)
print('Gaji Kotor \t\t: Rp', gKotor)
print('Zakat Profesi \t\t: Rp', int(zakat))
print('Take Home Pay \t\t: Rp', gBersih)
