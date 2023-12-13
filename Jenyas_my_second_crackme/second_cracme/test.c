#include <stdio.h>

void input(char *p) {
    gets(p);
}

int main(){
    char pass[4];
    char v5;
    input(pass);
    do {
        v5 = *pass;
        printf("%d ", v5);
        printf("%c ", v5);
        printf("\n");
        ++*pass;
    } while(*pass);

    return 0;
}