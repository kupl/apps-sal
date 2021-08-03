#include <stdio.h>

int main()
{
    int i,h;
    scanf("%d",&h);
    for(i=0;i<h;i++)
    {
        int a,b;
        scanf("%d%d",&a,&b);
        int x=0,y=0;
        while(a)
        {
            x=x*10+a%10;
            a/=10;
        }
        while(b)
        {
            y=y*10+b%10;
            b/=10;
        }
        x=x+y;
        y=0;
        while(x)
        {
            y=y*10+x%10;
            x/=10;
        }
        printf("%d ",y);
    }

    return 0;
}
