#include<stdio.h>
int main()
{
int n,i=0;
scanf("%d",&n);
int temp=n;
int sumof[n];
while(n!=0)
{ int a,b;
scanf("%d",&a);
scanf("%d",&b);
  int r,sum3=0,sum1=0,sum2=0,sum=0;
  while(a!=0)
  { r=a%10;
    sum1=sum1*10+r;
    a=a/10;
  }
  while(b!=0)
  {
  r=b%10;
  sum2=sum2*10+r;
  b=b/10;
  }
  sum=sum1+sum2;
  while(sum!=0)
  {
  r=sum%10;
  sum3=sum3*10+r;
  sum=sum/10;
  }
  sumof[i]=sum3;
  i++;
  n--;
  }
  for(i=0;i<temp;i++)
  {printf("%d\t",sumof[i]);
  }
  return 0;
}

