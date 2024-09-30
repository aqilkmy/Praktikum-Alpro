import os
os.system('cls')

jml_pakaian = int(input("Masukkan jumlah pakaian Pak Budi: "))
drop_pakaian = 5

jarak = 0

baju = 85000
celana = 100000
jaket = 155000

total_baju = 0
total_celana = 0
total_jaket = 0

print(f"Drop awal : {drop_pakaian}")
while jml_pakaian >= drop_pakaian :
    
    for i in(range(drop_pakaian)):
        jenis_pakaian = i % 3
        print(jenis_pakaian)
        if jenis_pakaian == 0:
            total_baju += 1
        elif jenis_pakaian == 1:
            total_celana += 1
        elif jenis_pakaian == 2:
            total_jaket += 1
    
    print(f"Jmlh pakaian : {jml_pakaian}")
    print(f"Drop selanjutnya : {drop_pakaian}")

    jml_pakaian = jml_pakaian - drop_pakaian + 4
    jarak += 15
    drop_pakaian += 2

total_harga_baju = total_baju * baju
total_harga_celana = total_celana * celana
total_harga_jaket = total_jaket * jaket

total_harga = total_harga_baju + total_harga_celana + total_harga_jaket
if jml_pakaian < drop_pakaian:
    print(f"Total harga : {total_harga}")
    print(f"Baju : {total_harga_baju} x{total_baju}")
    print(f"Celaana : {total_harga_celana} x{total_celana}")
    print(f"Jaket : {total_harga_jaket} x{total_jaket}")
    print(f"Sisa pakaian : {jml_pakaian}")
    print(f"Jarak ditempuh : {jarak} km")