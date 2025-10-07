class Rectangle:
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar

    def luas(self):
        " menghitung luas persegi panjang: panjang * lebar "
        return self.panjang * self.lebar 
    
    def keliling(self):
        " menghitung keliling persegi panjang: 2 *(panjang + lebar) "
        return 2 * (self.panjang + self.lebar)
    
panjang = float(input("masukan panjang persegi panjang: "))
lebar = float(input("masukan lebar persegi panjang: "))

persegi = Rectangle (panjang, lebar)
print(f"\nLuas persegi panjang: {persegi.luas()}")
print(f"Keliling persegi panjang: {persegi.keliling()}")
