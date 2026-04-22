# Bagian 1: Verifikasi Nama
nama_pendek = "Arya"

while True:
    input_nama = input("Masukan nama anda : ")
    
    if input_nama == nama_pendek:
        print("Nama benar! Lanjut ke program selanjutnya...\n")
        break
    else:
        print("silahkan coba lagi")

# Bagian 2: Tabel Perkalian
try:
    angka = int(input("Masukkan angka: "))
    
    print(f"Tabel Perkalian {angka}:")
    # Loop dari 1 sampai 10
    for i in range(1, 11):
        hasil = angka * i
        print(f"{angka} x {i} = {hasil}")
        
except ValueError:
    print("Mohon masukkan angka yang valid.")
