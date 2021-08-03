#include <stdio.h>

int rev(int a)
{
    int rem=0,reva=0;
   while(a!=0)
        {
            rem=a%10;
            reva=reva*10+rem;
            a/=10;
        } 
        return reva;
}


int main(void)
{
    int n,i,a,b,reva,revb,ans;
    scanf("%d",&n);
    for (i=0;i<n;i++)
    {
        scanf("%d%d",&a,&b);
        ans=rev(a)+rev(b);
        printf("%d ",rev(ans));
    }
	
	return 0;
}


