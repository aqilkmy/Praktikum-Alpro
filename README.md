# Praktikum-Alpro-2
Mekanisme pembelian pada toko sembako

	Deskripsi :
Athallah disuruh ibunya ke warung untuk membeli sembako. Lebih jelasnya ia disuruh untuk membeli Beras, Minyak, Telur, Gula, Garam, dan Cabe.
Namun sewajarnya sebuah warung belum tentu menyediakan stok yang cukup untuk kebutuhan konsumennya. Jadi jika jumlah barang yang ingin dibeli Athallah lebih dari stok yang tersedia, Athallah akan membeli sejumlah stok yang tersedia, namun jika stok mencukupi Athallah akan membeli sejumlah yang disuruh Ibunya.

Ibu Athallah memberikan uang Rp. 500.000 kepada Athallah, lebih tepatnya pecahan 5 x Rp. 100.000. Ibu Athallah kurang suka recehan, jadi ia berpesan agar kembaliannya diprioritaskan pecahan terbesar yang memungkinkan. Anda diminta untuk menentukan apakah UANG PAS, ADA KEMBALIAN, atau ATHALLAH NGUTANG. Jika ADA KEMBALIAN maka cetak pecahan-pecahan uangnya mulai dari yang terbesar. Dan jika ATHALLAH NGUTANG maka cetak berapa utangnya. 

Catatan : 
Harga masing masing barang :
Beras   (kg)        : Rp. 14.500
Minyak  (liter)     : Rp. 20.000
Telur   (kg)        : Rp. 25.000
Gula    (kg)        : Rp. 17.200
Garam   (kg)        : Rp. 9.800
Cabe    (kg)        : Rp. 23.000

Pecahan uang yang berlaku : 100, 200, 500, 1.000, 2.000, 5.000, 10.000, 20.000, 50.000, dan 100.000

Case "ADA KEMBALIAN" :
Maksud kembalian termasuk uang yang tidak dibayar ke penjual. Misal harga total adalah 98.000, maka wajarnya anda hanya akan memberikan pecahan 100.000 x 1 ke penjual, namun anda tetap perlu mencetak 100.000 x 4 pada keluaran programan. Dan hanya pecahan yang dipakai saja yang dicetak, misal di harga total 98.000 anda tidak perlu mencetak 10.000 x 0. Untuk lebih jelasnya bagaimana anda harus mencetak keluaran silahkan lihat contoh 2.


Contoh Input dan Output : 

Contoh 1 :

Input :
Jumlah Beras yang dibeli (kg) : 30
Jumlah Minyak yang dibeli (liter) : 3
Jumlah Telur yang dibeli (kg) : 4
Jumlah Gula yang dibeli (kg) : 1
Jumlah Garam yang dibeli (kg) : 1
Jumlah Cabe yang dibeli (kg) : 1

Stok Beras yang tersedia (kg) : 20
Stok Minyak yang tersedia (liter) : 10
Stok Telur yang tersedia (kg) : 15
Stok Gula yang tersedia (kg) : 7
Stok Garam yang tersedia (kg) : 5
Stok Cabe yang tersedia (kg) : 8

Output :
UANG PAS


Contoh 2 :

Input :
Jumlah Beras yang dibeli (kg) : 5
Jumlah Minyak yang dibeli (liter) : 3
Jumlah Telur yang dibeli (kg) : 6
Jumlah Gula yang dibeli (kg) : 1
Jumlah Garam yang dibeli (kg) : 1
Jumlah Cabe yang dibeli (kg) : 1

Stok Beras yang tersedia (kg) : 8
Stok Minyak yang tersedia (liter) : 2
Stok Telur yang tersedia (kg) : 4
Stok Gula yang tersedia (kg) : 7
Stok Garam yang tersedia (kg) : 5
Stok Cabe yang tersedia (kg) : 0

Output :
ADA KEMBALIAN
Pecahan Kembalian : 100.000 x 2, 50.000 x 1, 10.000 x 1, 500 x 1


Contoh 3 :

Input :
Jumlah Beras yang dibeli (kg) : 50
Jumlah Minyak yang dibeli (liter) : 8
Jumlah Telur yang dibeli (kg) : 10
Jumlah Gula yang dibeli (kg) : 2
Jumlah Garam yang dibeli (kg) : 2
Jumlah Cabe yang dibeli (kg) : 8

Stok Beras yang tersedia (kg) : 30
Stok Minyak yang tersedia (liter) : 10
Stok Telur yang tersedia (kg) : 15
Stok Gula yang tersedia (kg) : 2
Stok Garam yang tersedia (kg) : 5
Stok Cabe yang tersedia (kg) : 3

Output :
ATHALLAH NGUTANG
Jumlah Utang : Rp. 468000
