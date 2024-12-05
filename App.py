class nilaiMahasisa:
    def _init_(self):
        self.mhs = []

    def tambahData(self,nama,nilai):
        newObject = {
            "nama":nama,
            "nilai":nilai
        }
        self.mhs.append(newObject)

    def tampilkanData(self):
        for index,data in enumerate(self.mhs,1):
            print(f''' {index} | {data['nama']}  {data["nilai"]}''')

    def hapusData(self,index):
        if 1 <= index <= len(self.mhs):
            print('Data Di hapus')
            del self.mhs[index - 1]
        else:
            print("Index tidak valid!")
 
    def editData(self, index, nama=None, nilai=None):
        if 1 <= index <= len(self.mhs):
            if nama is not None:
                self.mhs[index - 1]["nama"] = nama
            elif nilai is not None:
                self.mhs[index - 1]["nilai"] = nilai
            print("Data berhasil diedit")
        else:
            print("Index tidak valid!")

data = nilaiMahasisa()
while True :
    print('''
    1. Menambahkan Data
    2. Menghapus Data
    3. Mengedit Data
    4. Menampilkan Data
    ''')

    inputUser = int(input("Masukkan key yang dipilih : "))
    if inputUser == 1: 
        nama = input ('masukan nama : ')
        nilai = int(input("masukan index : "))
        data.tambahData(nama, nilai)
    elif inputUser == 2: 
        index = int(input("masukan index : "))
        data.hapusData(index)
    elif inputUser == 3: 
        index = int(input("masukan index : "))
        data.editData(index)
    elif inputUser == 4 : 
        data.tampilkanData()
    else : 
        print('Terimakasih')