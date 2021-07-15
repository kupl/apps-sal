#include <stdio.h>
#include<string.h>
#define MAXN 20050

int main(void) {
	// your code goes here
	int tt;
	scanf("%d",&tt);
	while(tt-->0){
	   char str1[MAXN],str2[MAXN];
	   int num1[MAXN],num2[MAXN];
	   for(int i=0;i<MAXN;i++){
	       str1[i]='0';
	   }
	   for(int i=0;i<MAXN;i++){
	       str2[i]='0';
	   }
	   for(int i=0;i<MAXN;i++){
	       num1[i]=0;
	   }
	   for(int i=0;i<MAXN;i++){
	       num2[i]=0;
	   }
	   scanf("%s",str1);
	   scanf("%s",str2);
	   int i=0;
	   while(str1[i]){
	       num1[i]=str1[i]-'0';
	       i++;
	   }
	   i=0;
	   while(str2[i]){
	       num2[i]=str2[i]-'0';
	       i++;
	   }
	   int res[MAXN]={0};
	   int carry=0;
	   i=0;
	   for(int i=0;i<MAXN;i++){
	       int sum = num1[i]+num2[i]+carry;
	       res[i]=sum%10;
	       carry=sum/10;
	   }
	   i=0;
	   while(i<MAXN && res[i]==0){
	       i++;
	   }
	   int j=MAXN-1;
	   while(j>=0 && res[j]==0){
	       --j;
	   }
	   for(int k=i;k<=j;k+=1){
	       printf("%d",res[k]);
	   }
	   printf(" ");
	}
	return 0;
}


