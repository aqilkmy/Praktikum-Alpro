'''Soal 1: Menampilkan Bilangan Genap
Buatlah program yang menggunakan for loop untuk menampilkan semua bilangan 
genap antara 1 hingga 50.'''


def soal1():
    # bil = int(input("Masukkan bilangan: "))

    bil = 50

    for i in(range(1,bil+1)):
        if i % 2 == 0: 
            print(i)

''' Soal 2: Menjumlahkan Deret Bilangan
Buatlah program menggunakan while loop yang menjumlahkan semua bilangan dari 1 
hingga bilangan yang diinput oleh pengguna'''

def soal2():
    n = int(input("Masukkan bilangan: "))
    jumlah = 0
    for i in(range(1,n+1)):
        jumlah += i
    print(jumlah)

'''Soal 3: 
Mencari Nilai Terkecil. Buatlah program menggunakan for loop yang
menerima input bilangan dari pengguna sebanyak 10 kali dan mencari bilangan terkecil lalu tampilkan
'''

def soal3():
    x = int(input("Masukkan bilangan ke 1 : "))

    for i in(range(1,10)):
        y = int(input(f"Masukkan bilangan ke {i+1} : "))
        if x < y:
            x = x
            # print(f"Bilangan terkecil saat ini : {x} ")
        elif x == y:
            # print(f"Bilangan {x} sama dengan {y}")
            pass
        else:
            x = y
            # print(f"Bilangan terkecil saat ini : {y}")

    print(f"Bilangan terkecil: {x}")

print("\nSOAL 1: ")
soal1()
print("\nSOAL 2: ")
soal2()
print("\nSOAL 3: ")
soal3()
    