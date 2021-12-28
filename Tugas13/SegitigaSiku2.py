from Shape import *
from math import sqrt as akar

class Segi3Siku2(Shape):
    a = 0
    t = 0

    def __init__(self, nama, alas, tinggi):
        super().__init__(nama)
        self.a = alas
        self.t = tinggi

    def hitLuas(self):
        return self.a * self.t / 2

    def hitKeliling(self):
        return self.a + self.t + self.sisiMiring(self.a, self.t)
    
    def sisiMiring(self, a, t):
        return akar(a**2 + t**2)

    def cetak(self):
        super().cetak()
        print(f'''
    Alas : {self.a} | Tinggi : {self.t}
    Luas : {self.hitLuas()}
    Keliling : {self.hitKeliling()}
        ''')
