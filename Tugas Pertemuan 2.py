
import os
os.system('cls')

def menu():
    jml_uang = int(input("Masukkan jumlah uang yang dimiliki: "))
    harga_beras = 14500
    harga_minyak = 20000
    harga_telur = 25000
    harga_gula = 17200
    harga_garam = 9800
    harga_cabe = 23000

    stok_beras = 20
    stok_minyak = 10
    stok_telur = 15
    stok_gula = 7
    stok_garam = 5
    stok_cabe = 8

    print("Harga masing masing barang : \n")
    print(f"Beras   (kg)        : Rp. 14.500,  stok : {stok_beras}")
    print(f"Minyak  (liter)     : Rp. 20.000,  stok : {stok_minyak}")
    print(f"Telur   (kg)        : Rp. 25.000,  stok : {stok_telur}")
    print(f"Gula    (kg)        : Rp. 17.200,  stok : {stok_gula}")
    print(f"Garam   (kg)        : Rp. 9.800 ,  stok : {stok_garam}")
    print(f"Cabe    (kg)        : Rp. 23.000,  stok : {stok_cabe}\n")

    return jml_uang, harga_beras, harga_minyak, harga_telur, harga_gula, harga_garam, harga_cabe, stok_beras, stok_minyak, stok_telur, stok_gula, stok_garam, stok_cabe

def user_input():
    print("Masukkan jumlah barang yang ingin dibeli: \n")
    jml_beras = int(input(f"Beras   (kg)        : "))
    jml_minyak = int(input(f"Minyak  (liter)     : "))
    jml_telur = int(input(f"Telur   (kg)        : "))
    jml_gula = int(input(f"Gula    (kg)        : "))
    jml_garam = int(input(f"Garam   (kg)        : "))
    jml_cabe = int(input(f"Cabe    (kg)        : "))
    return jml_beras, jml_minyak, jml_telur, jml_gula, jml_garam, jml_cabe

def check_item(a, b, c):
    # a = jumlah barang, b = stok, c = harga, hasil = total harga 1 barang
    hasil = 0
    if a <= b and a >= 0:
        hasil = a * c
    else:
        hasil = b * c
    return hasil

def pecahan_uang(kembalian):
    pecahan = [100000, 50000, 20000, 10000, 5000, 2000, 1000, 500, 200, 100]
    hasil_pecahan = []
    
    for p in pecahan:
        jumlah = kembalian // p
        if jumlah > 0:
            hasil_pecahan.append((p, jumlah))
            kembalian -= p * jumlah
    
    return hasil_pecahan

def hitung_uang(jml_uang, total_harga):
    print(f"\nTotal harga: {total_harga}")
    if jml_uang > total_harga:
        kembalian = jml_uang - total_harga
        print("Ada kembalian")
        print(f"Kembalian : Rp. {kembalian}")
        pecahan = pecahan_uang(kembalian)
        pecahan_str = ", ".join([f"{p} x {j}" for p, j in pecahan])
        print(f"Pecahan Kembalian (Rp.): {pecahan_str}")
    elif jml_uang == total_harga:
        print('Uang pas')
    else:
        hutang = total_harga - jml_uang
        print(f"Hutang : - Rp. {hutang}")

# Menampilkan menu dan mendapatkan harga serta stok
jml_uang, harga_beras, harga_minyak, harga_telur, harga_gula, harga_garam, harga_cabe, stok_beras, stok_minyak, stok_telur, stok_gula, stok_garam, stok_cabe = menu()

# Mendapatkan input dari pengguna
jml_beras, jml_minyak, jml_telur, jml_gula, jml_garam, jml_cabe = user_input()

# Menghitung total harga masing-masing barang
total_beras = check_item(jml_beras, stok_beras, harga_beras)
total_minyak = check_item(jml_minyak, stok_minyak, harga_minyak)
total_telur = check_item(jml_telur, stok_telur, harga_telur)
total_gula = check_item(jml_gula, stok_gula, harga_gula)
total_garam = check_item(jml_garam, stok_garam, harga_garam)
total_cabe = check_item(jml_cabe, stok_cabe, harga_cabe)
total_harga = (total_beras + total_minyak + total_telur + total_gula + total_garam + total_cabe)

# Menghitung kembalian atau hutang
hitung_uang(jml_uang, total_harga)
