import os
os.system('cls')

angka = int(input("Masukkan angka yang akan difaktorialkan: "))


def faktorial_ganjil(angka):
    jumlah = 0
    for i in(range(1,angka+1)):
        if i % 2 != 0:
            jumlah = jumlah + faktorial(i)
    return jumlah



def faktorial(i):
    hasil = 1
    for i in (range(1, i+1)) :
        hasil = hasil * i
    return hasil

print(f"Hasil pemfaktoran: {faktorial_ganjil(angka)}")