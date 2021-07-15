t=int(input())
while(t>0):
    q=0
    a=input()
    n=len(a)
    for i in range(n//2):
        if(a[i]!=a[n-i-1]):
            q=1
            print(2)
            break
    if(q==0):
        print(1)
    t-=1
