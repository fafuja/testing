#include <stdio.h>
#define pprint(T) _Generic((T), 	\
	int: printf("%d \n", T), 	\
	float: printf("%f \n", T),	\
	char: printf("%c \n", T)	\
	)

int main(void){
	char c = 'a';
	pprint(c);
	return 0;
}

