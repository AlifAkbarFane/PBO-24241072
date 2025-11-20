class RekeningBank:
    def __init__(self, nama, saldo):
        self.nama = nama
        self.__saldo = saldo 

    
akun_budi = RekeningBank("Budi", 1000000)
try:
    print(f"saldo awal budi {akun_budi.saldo}")
except Exception as e:
    print("anda tidak dapat melihat saldo")

