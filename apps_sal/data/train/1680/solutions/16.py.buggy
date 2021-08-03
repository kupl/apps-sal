#include<stdio.h>

int reverse_number(int n)
{
    int r=0, a;
    while(n>=1)
    {
        a=n%10;
        r=r*10+a;
        n=n/10;
    }
    return r;
}

int main()
{
    int n , i , x , y;
    int r , s , t;
    scanf("%d", &n);

    for (i=0 ; i<n; i++)
    {
        scanf("%d", &x);
        scanf("%d", &y);
        
        r = reverse_number(x);
        s = reverse_number(y);
    
        t = reverse_number(r+s);
        printf("%d\n", t );
    }
    return 0;
}

