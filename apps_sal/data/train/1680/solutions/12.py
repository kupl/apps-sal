#include <stdio.h>
int reverse(int a)
{
    int r=0;
    while(a%10==0)
    {
        a/=10;
    }
    
    while(a>0)
    {
        r=r*10+a%10;
        a/=10;
    }
    
    return r;
    
}

int main() {
	int n;
	scanf("%d",&n);
	while(n>0)
	{
	    int a,b,sum;
	    scanf("%d %d",&a,&b);
	    sum=reverse(a)+reverse(b);
	    sum=reverse(sum);
	    printf("%d ",sum);
	    
	    n--;
	}
	return 0;
}


