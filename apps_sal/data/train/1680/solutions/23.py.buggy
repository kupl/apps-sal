#include <stdio.h>

int main(void) {
	// your code goes here
	int testcases;
	scanf("%d", &testcases);
	for(int i=0; i<testcases; i++) {
	    long long int a,b, a1=0, b1=0, sum1, res=0, rem;
	    scanf("%lld%lld", &a, &b);
	    while(a>0) {
	        rem=a%10;
            a1=a1*10+rem;
            a=a/10;
	    }
        while(b>0) {
            rem=b%10;
            b1=b1*10+rem;
            b=b/10;
        }
        sum1=a1+b1;
        while(sum1>0) {
            rem=sum1%10;
            res=res*10+rem;
            sum1=sum1/10;
        }
        printf("%lld\n", res);
	}
	return 0;
}


