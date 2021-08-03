#include <stdio.h>
int rev(int x){
    int rn=0;
    while(x!=0){
        int re=x%10;
        rn=rn*10+re;
        x/=10;
    }
    return rn;
}
int main(void) {
	// your code goes here
	 int n;
    scanf("%d",&n);
    while(n--)
    {
        int p,q;
        scanf("%d %d",&p,&q);
        int k=rev(p)+rev(q);
        printf("%d ",rev(k));
    }
	return 0;
}


