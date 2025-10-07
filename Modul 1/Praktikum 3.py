class Mahasiswa: 
    
    jumlah_mahasiswa = 0
    
    def __init__(self, name, nim, prodi): 
        self.name = name 
        self.nim = nim 
        self.prodi = prodi
        Mahasiswa.jumlah_mahasiswa += 1
        print(f"Membuat Object Mahasiswa ke-{Mahasiswa.jumlah_mahasiswa}, dengan nama{self.name}")
        
mhs1 = Mahasiswa(" irfan", "2345112", "Manajement")
mhs2 = Mahasiswa(" ali", "2435142", "Teknik Industri")
mhs3 = Mahasiswa(" Hengky", "2314524", "Ilmu Hukum")

print(f"\ntotal mahasiswa: " + str(Mahasiswa.jumlah_mahasiswa))