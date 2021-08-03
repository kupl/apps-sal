#include<stdio.h>

int reverse(long long int num)
{
	long long int temp=0;
	long long int rev=0;
	while(num>0)
	{
		temp=num%10;
		rev=10*rev+temp;
		num=num/10;
	}
	return rev;
}
int main()
{	
	long long int n;
	scanf("%lld",&n);
	for(int i=0;i<n;i++)
	{
		long long int a,b,sum;
		scanf("%lld",&a);
		scanf("%lld",&b);
		sum=reverse(a)+reverse(b);
		printf("%lld",reverse(sum));
		printf(" ");
		
		
	}
	
}
