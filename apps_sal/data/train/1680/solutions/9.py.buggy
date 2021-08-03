
#include <stdio.h>

int reversDigits(int num) 
{ 
    int rev_num = 0; 
    while(num > 0) 
    { 
        rev_num = rev_num*10 + num%10; 
        num = num/10; 
    } 
    return rev_num; 
} 

int main(void) {
 int N;
 scanf("%d",&N);
 for(int i=0;i<N;i++)
 {
  int p,q,sum,rev_sum;
  scanf("%d",&p);
  scanf("%d",&q);
  sum=reversDigits(p)+ reversDigits(q);
  rev_sum=reversDigits(sum);
  printf("%d",rev_sum);
  printf(" ");

 }
	// your code goes here
	return 0;
}


