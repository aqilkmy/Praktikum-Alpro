#include <stdio.h>
// #include <stdlib.h>

// int bil = 50;
// int main() {
//     for (int i = 1;i<=50;i++)
//         if (i % 2 == 0) {
//             printf(" %d",i);
//         }
// }

/*
int n, jumlah;

int main(){
    printf("Masukkan bilangan       : ");
    scanf("%d", &n);
    for (int i=1 ; i<=n ; i++) {
        jumlah += i;
    }
    printf("%d", jumlah);
}
*/

int x,y;
int main(){
    printf("Masukkan bilangan ke 1: ");
    scanf("%d",&x);

    for (int i = 1 ; i < 10 ; i++){
        printf("Masukkan bilangan ke %d : ", i+1);
        scanf("%d", &y);

        if (x < y){
            x = x;
        }
        // else if (x==y){
        //     x = x;
        // }
        else {
            x = y;
        }
    }
    printf("Bilangan terkecil : %d", x);
}