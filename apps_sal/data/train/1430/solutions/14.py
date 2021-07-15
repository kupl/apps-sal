t=int(input())
while t>0:
    n,k=map(int,input().split())
    if n%2==0:
        ans=(n//2)*(2+k)
    else:
        ans=((n//2)*(2+k))+(2*k+1)
    print(int(ans))
    t-=1
