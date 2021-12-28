from Shape import *
class Lingkaran(Shape):
    r = 0

    def __init__(self, nama, r):
        super().__init__(nama)
        self.r = r
        self.phi = (3.14, 22/7)[self.r %7 == 0]

    def hitLuas(self):
        return self.phi * self.r**2
    
    def hitKeliling(self):
        return 2 * self.phi * self.r

    def cetak(self):
        super().cetak()
        print(f'''
    Jari-jari (r) : {self.r}
    Luas : {self.hitLuas()}
    Keliling : {self.hitKeliling()}
        ''')

