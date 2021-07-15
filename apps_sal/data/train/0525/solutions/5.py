n=int(input())
for i in range(n):
    abc=list(map(int,input().split()))
    a=abc[0];b=abc[1];c=abc[2]
    l=c-(c%a)
    if((l+b)>c):
        l=l-a
    if(a<=b):
        l=0
    print(l+b)

