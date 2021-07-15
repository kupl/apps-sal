#include <stdio.h>

	int main()
{
    int n;
    scanf("%d", &n);
    for(int i=0; i<n; i++)
    {
      int a, b;
        scanf("%d %d", &a, &b);
        int x;
    int rev1=0, rev3=0;
        while(a!=0)
        {
            x=a%10;
           rev1=rev1*10+x;
           a=a/10;
        }
    int rev2=0;
        while(b!=0)
        {
            x=b%10;
           rev2=rev2*10+x;
           b=b/10;
        }
        int y=rev1+rev2;
        while(y!=0)
        {
            x=y%10;
           rev3=rev3*10+x;
           y=y/10;
        }
        printf("%d ", rev3);

    }
}


