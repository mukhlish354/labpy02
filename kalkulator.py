
# Mendefinisikan operasi aritmatika
def penjumlahan(a, b):
    return a + b

def pengurangan(a, b):
    return a - b

def perkalian(a, b):
    return a * b

def pembagian(a, b):
    if b != 0:
        return a / b
    else:
        return "Pembagian tidak bisa menggunakan 0"

# Fungsi utama untuk menjalankan kalkulator
def kalkulator():
    print("--------------------------")
    print("--- Kalkulator Sederhana ---")
    print("--------------------------")
    
    print("Pilih operasi:")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")
    print("5. Keluar")
    
    # Memilih jenis operasi
    pilihan = input("Masukkan pilihan (1/2/3/4/5): ")
    
    # Cek pilihan untuk keluar atau pilihan yang tidak valid
    if pilihan == '5':
        print("Anda keluar dari kalkulator.")
        return
    elif pilihan > '5' or pilihan <= '0' or pilihan == '':
        print("Pilihan yang dipilih tidak valid!")
        return
    
    # Memasukkan angka dan validasi input
    try:
        angka1 = int(input("Masukkan angka pertama: "))
        angka2 = int(input("Masukkan angka kedua: "))
    except ValueError:
        print("Anda tidak memasukkan angka yang valid!")
        return
    
    # Proses dan hasil berdasarkan pilihan operasi
    if pilihan == '1':
        hasil = penjumlahan(angka1, angka2)
        print("Hasil penjumlahan =", hasil)
    elif pilihan == '2':
        hasil = pengurangan(angka1, angka2)
        print("Hasil pengurangan =", hasil)
    elif pilihan == '3':
        hasil = perkalian(angka1, angka2)
        print("Hasil perkalian =", hasil)
    elif pilihan == '4':
        hasil = pembagian(angka1, angka2)
        print("Hasil pembagian =", hasil)

# Menjalankan program kalkulator
kalkulator()
