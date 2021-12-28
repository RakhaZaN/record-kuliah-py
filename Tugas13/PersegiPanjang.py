from Shape import *

class PersegiPanjang(Shape):
    p = 0
    l = 0

    def __init__(self, nama, panjang, lebar):
        super().__init__(nama)
        self.p = panjang
        self.l = lebar

    def hitLuas(self):
        return self.p * self.l

    def hitKeliling(self):
        return 2*self.l + 2*self.p

    def cetak(self):
        super().cetak()
        print(f'''
    Panjang : {self.p} | Lebar = {self.l}
    Luas : {self.hitLuas()}
    Keliling : {self.hitKeliling()}
        ''')
