#include<stdio.h>
int reverse(int a)
{   
    int sum =0;
 	 while(a>0)
	  {
	  	   sum =sum*10 + (a%10);
			  a = a/10; 	  
	  }	
	  return sum;
}
int main(){
	int n;
	int a,b;
	scanf("%d",&n);
	for(int i=0;i<n;i++){
		scanf("%d%d",&a,&b);
		a=reverse(a);
		b=reverse(b);
		printf("%d ",reverse(a+b));
	}
}
