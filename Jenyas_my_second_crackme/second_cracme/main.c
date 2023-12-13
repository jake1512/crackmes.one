#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
extern int check_numbers_letters(char* p);
extern int check_len(char* p);
extern int check_calc(char* p);
void input(char *p) {
	printf("Enter passowrd: ");
	gets(p);
}
void run(){
	char pass[100];
	input(pass);
	if (check_len(pass) && check_numbers_letters(pass) && check_calc(pass))
		puts("Correct");
	else
		puts("Wrong");
}
void main() {
	run();
	system("pause>0");
}