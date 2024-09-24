#include <stdio.h>
#include <stdlib.h>

void menu(int *jml_uang, int *harga_beras, int *harga_minyak, int *harga_telur, int *harga_gula, int *harga_garam, int *harga_cabe, int *stok_beras, int *stok_minyak, int *stok_telur, int *stok_gula, int *stok_garam, int *stok_cabe) {
    
    printf("Masukkan jumlah uang yang dimiliki: ");
    scanf("%d", jml_uang);

    *harga_beras = 14500;
    *harga_minyak = 20000;
    *harga_telur = 25000;
    *harga_gula = 17200;
    *harga_garam = 9800;
    *harga_cabe = 23000;

    *stok_beras = 20;
    *stok_minyak = 12;
    *stok_telur = 2;
    *stok_gula = 7;
    *stok_garam = 5;
    *stok_cabe = 8;

    printf("Harga masing masing barang : \n");
    printf("Beras   (kg)        : Rp. 14.500,  stok : %d\n", *stok_beras);
    printf("Minyak  (liter)     : Rp. 20.000,  stok : %d\n", *stok_minyak);
    printf("Telur   (kg)        : Rp. 25.000,  stok : %d\n", *stok_telur);
    printf("Gula    (kg)        : Rp. 17.200,  stok : %d\n", *stok_gula);
    printf("Garam   (kg)        : Rp. 9.800 ,  stok : %d\n", *stok_garam);
    printf("Cabe    (kg)        : Rp. 23.000,  stok : %d\n", *stok_cabe);
}

void user_input(int *jml_beras, int *jml_minyak, int *jml_telur, int *jml_gula, int *jml_garam, int *jml_cabe) {
    printf("Masukkan jumlah barang yang ingin dibeli: \n");
    printf("Beras   (kg)        : ");
    scanf("%d", jml_beras);
    printf("Minyak  (liter)     : ");
    scanf("%d", jml_minyak);
    printf("Telur   (kg)        : ");
    scanf("%d", jml_telur);
    printf("Gula    (kg)        : ");
    scanf("%d", jml_gula);
    printf("Garam   (kg)        : ");
    scanf("%d", jml_garam);
    printf("Cabe    (kg)        : ");
    scanf("%d", jml_cabe);
}

int check_item(int a, int b, int c) {
    int hasil = 0;
    if (a <= b && a >= 0) {
        hasil = a * c;
    } else {
        hasil = b * c;
    }
    return hasil;
}

void pecahan_uang(int kembalian) {
    int pecahan[] = {100000, 50000, 20000, 10000, 5000, 2000, 1000, 500, 200, 100};
    int jumlah;
    printf("Pecahan Kembalian (Rp.): ");
    for (int i = 0; i < 10; i++) {
        jumlah = kembalian / pecahan[i];
        if (jumlah > 0) {
            printf("%d x %d, ", pecahan[i], jumlah);
            kembalian -= pecahan[i] * jumlah;
        }
    }
    printf("\n");
}

void hitung_uang(int jml_uang, int total_harga) {
    printf("Total harga: %d\n", total_harga);
    if (jml_uang > total_harga) {
        int kembalian = jml_uang - total_harga;
        printf("Ada kembalian\n");
        pecahan_uang(kembalian);
    } else if (jml_uang == total_harga) {
        printf("Uang pas\n");
    } else {
        int hutang = total_harga - jml_uang;
        printf("Hutang : Rp. %d\n", hutang);
    }
}

int main() {
system("cls");
    int jml_uang, harga_beras, harga_minyak, harga_telur, harga_gula, harga_garam, harga_cabe;
    int stok_beras, stok_minyak, stok_telur, stok_gula, stok_garam, stok_cabe;
    int jml_beras, jml_minyak, jml_telur, jml_gula, jml_garam, jml_cabe;

    menu(&jml_uang, &harga_beras, &harga_minyak, &harga_telur, &harga_gula, &harga_garam, &harga_cabe, &stok_beras, &stok_minyak, &stok_telur, &stok_gula, &stok_garam, &stok_cabe);
    user_input(&jml_beras, &jml_minyak, &jml_telur, &jml_gula, &jml_garam, &jml_cabe);

    int total_beras = check_item(jml_beras, stok_beras, harga_beras);
    int total_minyak = check_item(jml_minyak, stok_minyak, harga_minyak);
    int total_telur = check_item(jml_telur, stok_telur, harga_telur);
    int total_gula = check_item(jml_gula, stok_gula, harga_gula);
    int total_garam = check_item(jml_garam, stok_garam, harga_garam);
    int total_cabe = check_item(jml_cabe, stok_cabe, harga_cabe);
    int total_harga = total_beras + total_minyak + total_telur + total_gula + total_garam + total_cabe;

    hitung_uang(jml_uang, total_harga);

    return 0;
}
