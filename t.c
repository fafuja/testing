#include <stdio.h>
#include <stdint.h>
typedef unsigned char byte;

int main(void){
	uint32_t a = 2143483647;
	byte *p = (byte*)&a;
	printf("%d", *p);
	printf("\n");
	printf("%d", *(int *)p);
	printf("\n");
	printf("%p", p);
	printf("\n Updating value... \n");
	*((uint32_t*) p) = 0;
	*((uint32_t*) p) = 1UL << 14;
	printf("%d", *(uint32_t *)p);
	printf("\n");
}
