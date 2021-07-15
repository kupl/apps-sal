import math
mod=(10**9)+7
T=int(input())
for _ in range(T):
    N,K=list(map(int,input().split()))
    if (N==0):
        print(((K*(K-1)))%mod)
    else:
        pos=(math.ceil((K-1)/2)+N)
        if ((K)%2==0 or K==1):
            et=N
        else:
            et=pos+pos-N
        t=((pos*(pos-1))+et)%mod
        print(t%mod)

