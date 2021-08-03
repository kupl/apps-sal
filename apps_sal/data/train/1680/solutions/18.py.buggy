#include <stdio.h>
int reverse(int n) {
    int rev = 0, remainder;
    
    
    while (n != 0) {
        remainder = n % 10;
        rev = rev * 10 + remainder;
        n /= 10;
    }
    
    return rev;
}

int main(void) {
    int i,no,n1,n2,large=0,j;
    scanf("%d \n",&no);
     for(i=1;i<=no;i++)
       {
           scanf("%d %d\n", &n1,&n2);
           int sum=reverse(n1)+reverse(n2);
           int ans=reverse(sum);
           printf("%d\n",ans);
           
       }
	// your code goes here
	return 0;
}


