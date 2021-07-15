#include <stdio.h>
#define ll long long
ll revese(ll n)
{
    ll rev = 0, remainder;
    while (n != 0) {
        remainder = n % 10;
        rev = rev * 10 + remainder;
        n /= 10;
    }
    return rev;
}

int main(void) {
    
    ll t;
    scanf("%ld",&t);
    while(t--)
    {
        ll n1,n2,sum;
        scanf("%ld %ld",&n1,&n2);
        sum = revese(n1) + revese(n2);
        printf("%ld\n",revese(sum));
    }
	
	return 0;
}


