## *Praktikum 8*

Program pertama yang akan dibuat adalah Program untuk menampilkan angka pertama dan kedua dan masukan operator dan mendapat hasil dari input

**Berikut flowchartnya**

![flowchart 1_praktikum8](https://github.com/user-attachments/assets/7c97e38e-1e00-4adb-8987-889d3905c821)

![flowchart 2_praktikum8](https://github.com/user-attachments/assets/9acb3a2e-1a17-4905-a897-f90b16d4a9e7)

*Program akan meminta kita untuk memasukkan nama, nim, nilai tugas, nilai uts, nilai uas dan tambah data :*

![output pemro8](https://github.com/user-attachments/assets/d34e08ef-b5ff-4434-af70-b4f8cfcd2b98)

**Penjelasan Code**
```

class DaftarMahasiswa:
    def __init__(self):
        self.data_mahasiswa = []

    def tambah(self):
        """Menambah data mahasiswa baru."""
        nama = input("Masukkan nama mahasiswa: ")
        nilai = float(input("Masukkan nilai mahasiswa: "))
        self.data_mahasiswa.append({"nama": nama, "nilai": nilai})
        print("Data mahasiswa berhasil ditambahkan.")

    def tampilkan(self):
        """Menampilkan semua data mahasiswa."""
        if not self.data_mahasiswa:
            print("Data mahasiswa masih kosong.")
        else:
            print("Daftar Nilai Mahasiswa:")
            print("--------------------------")
            for mahasiswa in self.data_mahasiswa:
                print(f"Nama: {mahasiswa['nama']}, Nilai: {mahasiswa['nilai']}")
                print("--------------------------")

    def hapus(self, nama):
        """Menghapus data mahasiswa berdasarkan nama."""
        for i, mahasiswa in enumerate(self.data_mahasiswa):
            if mahasiswa['nama'].lower() == nama.lower():
                del self.data_mahasiswa[i]
                print(f"Data mahasiswa dengan nama {nama} berhasil dihapus.")
                return
        print(f"Data mahasiswa dengan nama {nama} tidak ditemukan.")

    def ubah(self, nama):
        """Mengubah data mahasiswa berdasarkan nama."""
        for mahasiswa in self.data_mahasiswa:
            if mahasiswa['nama'].lower() == nama.lower():
                nilai_baru = float(input("Masukkan nilai baru: "))
                mahasiswa['nilai'] = nilai_baru
                print(f"Data mahasiswa dengan nama {nama} berhasil diubah.")
                return
        print(f"Data mahasiswa dengan nama {nama} tidak ditemukan.")

# Inisialisasi objek DaftarMahasiswa
daftar_mahasiswa = DaftarMahasiswa()

# Menu program
while True:
    print("\nMenu:")
    print("1. Tambah data mahasiswa")
    print("2. Tampilkan data mahasiswa")
    print("3. Hapus data mahasiswa")
    print("4. Ubah data mahasiswa")
    print("5. Keluar")
    pilihan = input("Pilih menu (1/2/3/4/5): ")

    if pilihan == '1':
        daftar_mahasiswa.tambah()
    elif pilihan == '2':
        daftar_mahasiswa.tampilkan()
    elif pilihan == '3':
        nama = input("Masukkan nama mahasiswa yang ingin dihapus: ")
        daftar_mahasiswa.hapus(nama)
    elif pilihan == '4':
        nama = input("Masukkan nama mahasiswa yang ingin diubah: ")
        daftar_mahasiswa.ubah(nama)
    elif pilihan == '5':
        print("Terima kasih! Program selesai.")
        break
    else:
        print("Pilihan tidak valid.")


**Penjelasan**
Kelas DaftarMahasiswa

init():

Fungsi ini merupakan constructor yang dijalankan saat objek DaftarMahasiswa dibuat.
Membuat list kosong data_mahasiswa untuk menyimpan data mahasiswa. Setiap elemen dalam list ini adalah dictionary yang berisi nama dan nilai mahasiswa.
tambah():

Fungsi ini digunakan untuk menambahkan data mahasiswa baru.
Meminta input nama dan nilai dari pengguna.
Membuat dictionary baru berisi nama dan nilai, kemudian menambahkannya ke dalam list data_mahasiswa.
tampilkan():

Fungsi ini digunakan untuk menampilkan semua data mahasiswa yang sudah tersimpan.
Jika list data_mahasiswa kosong, maka akan menampilkan pesan bahwa data masih kosong.
Jika ada data, maka akan menampilkan daftar nama dan nilai mahasiswa dalam format yang terbaca.
hapus():

Fungsi ini digunakan untuk menghapus data mahasiswa berdasarkan nama.
Melakukan pencarian pada list data_mahasiswa untuk menemukan data yang sesuai dengan nama yang diinputkan.
Jika data ditemukan, maka data tersebut akan dihapus dari list.
Jika data tidak ditemukan, maka akan menampilkan pesan bahwa data tidak ditemukan.
ubah():

Fungsi ini digunakan untuk mengubah nilai mahasiswa berdasarkan nama.
Melakukan pencarian pada list data_mahasiswa untuk menemukan data yang sesuai dengan nama yang diinputkan.
Jika data ditemukan, maka nilai mahasiswa akan diubah dengan nilai baru yang diinputkan oleh pengguna.
Jika data tidak ditemukan, maka akan menampilkan pesan bahwa data tidak ditemukan.
Program Utama

Inisialisasi objek: Membuat objek DaftarMahasiswa dengan nama daftar_mahasiswa.
Looping menu:
Menampilkan menu pilihan kepada pengguna.
Meminta pengguna untuk memilih menu yang diinginkan.
Berdasarkan pilihan pengguna, memanggil fungsi yang sesuai dari objek daftar_mahasiswa.
Looping akan terus berjalan sampai pengguna memilih untuk keluar.
Konsep Penting

Orientasi Objek: Program ini menggunakan konsep orientasi objek dengan membuat kelas DaftarMahasiswa. Kelas ini merepresentasikan kumpulan data dan fungsi-fungsi yang berhubungan dengan data tersebut.
List: Digunakan untuk menyimpan data mahasiswa dalam bentuk dictionary. List memungkinkan kita untuk menyimpan banyak data dalam satu variabel.
Dictionary: Digunakan untuk menyimpan data mahasiswa dalam bentuk pasangan kunci-nilai. Kunci digunakan untuk mengidentifikasi data, sedangkan nilai adalah data yang sebenarnya.
Fungsi: Fungsi digunakan untuk mengelompokkan kode yang melakukan tugas tertentu. Dengan menggunakan fungsi, kode menjadi lebih terstruktur dan mudah dibaca.
Keunggulan Kode

Terstruktur: Kode diorganisir dengan baik menggunakan kelas dan fungsi.
Mudah dipahami: Penggunaan komentar membantu menjelaskan setiap bagian kode.
Fleksibel: Kode dapat dengan mudah diperluas untuk menambahkan fitur-fitur baru.
Efisien: Penggunaan list dan dictionary membuat pencarian dan pengubahan data menjadi lebih efisien.
Peningkatan yang Mungkin Dilakukan

Validasi input: Menambahkan validasi input untuk memastikan bahwa data yang dimasukkan oleh pengguna valid (misalnya, nilai harus berupa angka).
Pengurutan: Menambahkan fitur untuk mengurutkan data mahasiswa berdasarkan nama atau nilai.
Pencarian: Menambahkan fitur untuk mencari data mahasiswa berdasarkan kriteria tertentu (misalnya, mencari semua mahasiswa dengan nilai di atas 80).
Penyimpanan data: Menambahkan fitur untuk menyimpan data mahasiswa ke dalam file, sehingga data tidak hilang ketika program dijalankan ulang.
