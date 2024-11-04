
# Mendefinisikan Harga Tiket Sesuai Tipe
reg = 50000
vip = 100000

# Menginput jenis tiket
jenis = input("Pilih jenis ticket anda (vip/reguler): ")

# Mendefinisikan Harga Sesuai Jenis Tiket 
if jenis == "vip":
    harga_ticket = vip
elif jenis == "reg":
    harga_ticket = reg
else:
    print("Input tidak valid")
    exit()

# Menghitung Total Harga
member = input("Apakah anda punya kartu member (ya/tidak): ")
harga_ticket -= harga_ticket * 0.20 if member == "ya" else 0

print(f"Harga ticket anda Rp. {int(harga_ticket)}")
