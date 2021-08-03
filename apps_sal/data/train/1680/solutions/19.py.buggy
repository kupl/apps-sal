#include<stdio.h>
int rev(int k)
{
int j,res=0;
while(k)
{
res=res*10+k%10;
k/=10;
}
return res;
}
int main()
{
int j,a,b,m,k;
while(scanf("%d",&m)!=EOF)
{
for(j=1;j<=m;j++)
{
scanf("%d %d",&a,&b);
k=rev(a)+rev(b);
printf("%d\n",rev(k));
}
}
return 0;
}

  
