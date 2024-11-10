import os
os.system('cls')




"""Soal 1: Menghitung Penjumlahan Bilangan Prima Buatlah sebuah fungsi jumlah_bilangan_prima(n) 
yang menerima sebuah bilangan bulat n dan mengembalikan nilai Penjumlahan dari semua bilangan prima 
yang kurang dari sama dengan n"""

def soal1():
    def is_prima(bil):
        if bil <= 1:
            return False
        for i in range(2, bil):
            if bil % i == 0:
                return False
        return True

    def jumlah_bilangan_prima(n):
        jumlah = 0
        for i in range(2, n + 1):
            if is_prima(i):
                jumlah += i
        return jumlah
    os.system('cls')
    print("SOAL 1: Menghitung jumlah bilangan prma <= n\n")
    n = int(input("Masukkan nilai n: "))
    hasil = jumlah_bilangan_prima(n)
    print(f"Hasil penjumlahan bilangan prima yang kurang dari sama dengan {n} adalah {hasil}")


'''Soal 2: Menghitung Jumlah Bilangan Genap Buatlah sebuah fungsi jumlah_bilangan_genap(n) yang menerima 
sebuah bilangan bulat n dan mengembalikan jumlah dari semua bilangan genap yang kurang dari  sama dengan n'''

def soal2():

    def jumlah_bilangan_genap(n):
        jumlah = 0
        for i in(range(1,n+1)):
                if i % 2 == 0:
                    jumlah += i
            
            
        return jumlah
    os.system('cls')
    print("SOAL 2 : Menghitung jumlah bilangan genap <= n \n")
    n = int(input("Input n:"))
    hasil = jumlah_bilangan_genap(n)
    print(hasil)

'''
Soal 3: Menghitung Jumlah Digit Ganjil dalam Bilangan
    Buatlah sebuah fungsi jumlah_digit_ganjil(x) yang menerima sebuah bilangan bulat x dan 
mengembalikan jumlah dari semua digit ganjil dalam bilangan tersebut. Namun, kali ini, 
jika tidak ada digit ganjil dalam bilangan tersebut, fungsi harus mengembalikan pesan “Tidak ada digit ganjil”.
'''
def soal3():
    def jumlah_digit_ganjil(n):
        jumlah = 0
        ada_ganjil = False
        while n > 0:
            digit = n % 10
            if digit % 2 != 0:
                jumlah += digit
                ada_ganjil = True
            n = n//10
        if ada_ganjil:
            return jumlah   
        else: 
             return "tidak ada digit ganjil pada bilangan" 
            
    os.system('cls')
    print("SOAL 3: Menghitung digit ganjil dari bilangan n")

    n = int(input("Masukkan nilai n: "))
    hasil = jumlah_digit_ganjil(n)
    print(f"Hasil penjumlahan digit bilangan {n} adalah {hasil}  ")


'''
Soal 4: Menghitung Jumlah Faktorial Bilangan Ganjil dalam Rentang

Buatlah sebuah fungsi faktorial_ganjil_rentang(a, b) yang menerima dua bilangan bulat a dan b, 
dan mengembalikan hasil penjumlahan faktorial dari semua bilangan ganjil yang berada dalam 
rentang a hingga b (termasuk a dan b jika ganjil).
'''

def soal4():
    def faktorial(i):
        hasil = 1
        for i in (range(1, i+1)) :
            hasil = hasil * i
        return hasil
    
    def rentang_faktorial_ganjil(a,b):
        jumlah = 0
        for i in(range(a,b+1)):
            if i % 2 != 0:
                jumlah = jumlah + faktorial(i)
        return jumlah

    os.system('cls')
    print("SOAL 4: Penjumlahan faktorial angka ganjil dari rentang 2 angka ")

    a = int(input("Masukkan batas awal: "))
    b = int(input("Masukkan batas akhir: "))
    hasil = rentang_faktorial_ganjil(a,b)
    print(f"Hasil penjumlahan faktorial angka ganjil dari angka {a} sampai {b} adalah {hasil}")




'''
Soal 5: Menghitung Jumlah Bilangan Pangkat dalam Rentang
Buatlah sebuah fungsi jumlah_bilangan_pangkat(a, b, p) yang menerima tiga bilangan bulat 
a, b, dan p, dan mengembalikan jumlah dari semua bilangan dalam rentang a hingga b yang
 dipangkatkan dengan p.
'''

def soal5():
    def pangkat(a,b,p):
        jumlah = 0
        for i in(range(a,b+1)):
            jumlah += i  ** p
        return jumlah

    os.system('cls')
    print("SOAL 5: Menghitung Jumlah Bilangan Pangkat dalam Rentang")

    a = int(input("Masukkan batas awal: "))
    b = int(input("Masukkan batas akhir: "))
    p = int(input("Masukkan pangkat: "))
    hasil = pangkat(a,b,p)
    print(f"Hasil penjumlahan dari angka {a} sampai dengan {b} dipangkatkan {p} adalah {hasil}")

menu = int(input("Masukkan nomor soal: "))
if menu == 1:
    soal1()
elif menu == 2:
    soal2()
elif menu == 3:
    soal3()
elif menu == 4:
    soal4()
elif menu == 5:
    soal5()