#include <stdio.h>
#include <stdlib.h>

int main() {
    char ulangi;
    do {
        system("cls");

        int jml_pakaian;
        printf("Masukkan jumlah pakaian Pak Budi: ");
        scanf("%d", &jml_pakaian);

        int drop_pakaian = 5;
        int jarak = 0;

        int baju = 85000;
        int celana = 100000;
        int jaket = 155000;

        int total_baju = 0;
        int total_celana = 0;
        int total_jaket = 0;

        printf("Drop awal : %d\n", drop_pakaian);
        while (jml_pakaian >= drop_pakaian) {
            printf("Tag pakaian di toko %d: \n", jarak / 15 + 1);
            for (int i = 0; i < drop_pakaian; i++) {
                int jenis_pakaian = i % 3;
                printf("%d\n", jenis_pakaian);
                if (jenis_pakaian == 0) {
                    total_baju++;
                } else if (jenis_pakaian == 1) {
                    total_celana++;
                } else if (jenis_pakaian == 2) {
                    total_jaket++;
                }
            }

            jml_pakaian = jml_pakaian - drop_pakaian + 4;
            jarak += 15;
            drop_pakaian += 2;
        }

        int total_harga_baju = total_baju * baju;
        int total_harga_celana = total_celana * celana;
        int total_harga_jaket = total_jaket * jaket;

        int total_harga = total_harga_baju + total_harga_celana + total_harga_jaket;
        if (jml_pakaian < drop_pakaian) {
            printf("Total harga : Rp%d\n", total_harga);
            printf("Baju : Rp%d x%d\n", total_harga_baju, total_baju);
            printf("Celana : Rp%d x%d\n", total_harga_celana, total_celana);
            printf("Jaket : Rp%d x%d\n", total_harga_jaket, total_jaket);
            printf("Sisa pakaian : %d\n", jml_pakaian);
            printf("Jarak ditempuh : %d km\n", jarak);
        }

        printf("Apakah Anda ingin mengulang? (y/n): ");
        scanf(" %c", &ulangi);
    } while (ulangi == 'y' || ulangi == 'Y');

    return 0;
}
