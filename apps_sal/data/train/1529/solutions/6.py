t=int(input())
def fac(x):
    if x==0:
        return 1
    else:
        return x*fac(x-1)
for j in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    s=0
    for i in range(n):
        for j in a:
            s+=(j*10**i)*(fac(n-1))
    print(s)
