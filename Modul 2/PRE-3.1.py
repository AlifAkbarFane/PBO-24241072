class Mobil:
    
    total_mobil_dibuat = 0 

    def __init__(self, nama):
        self.nama = nama 
        Mobil.total_mobil_dibuat += 1 

    def nyalakan_mesin(self):
        print(f"Mesin {self.nama} menyala!")

    @classmethod
    def get_total_produksi(cls):
        print(f"Pabrik telah memproduksi {cls.total_mobil_dibuat} unit mobil.")


Mobil.get_total_produksi() 

print("--- Membuat mobil ---")
Mustag= Mobil("Mustag")
Porsche  = Mobil("Porsche ")
Koenigsegg = Mobil("Koenigsegg")
Pagani = Mobil("Pagani")
print("---------------------")

Mobil.get_total_produksi()