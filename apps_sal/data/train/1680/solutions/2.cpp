#include<stdio.h>
//using namespace std;
#define lli long long int
//#define pb push_back
//#define rep(i,a,n) for(i=a;i<n;i++)

void solve()
{
	lli a,b;
	scanf("%ld%ld",&a,&b);
	lli c=0,d=0;
	while(a)
	{ 
      c=(c*10)+(a%10);
      a/=10;
	}
	while(b)
	{ 
      d=(d*10)+(b%10);
      b/=10;
	}
	//cout<<c<<" "<<d<<" ";
	c+=d;
	a=c;
	c=0;
	while(a)
	{ 
      c=(c*10)+(a%10);
      a/=10;
	}
	printf("%ld ",c);
}
int main()
{
   // ios::sync_with_stdio(0);
    //cin.tie(0);cout.tie(0);
	lli t=1;
	scanf("%ld",&t);
	while(t--)
	{
      solve();
	}
	return 0;
}
