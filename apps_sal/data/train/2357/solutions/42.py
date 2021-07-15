MOD=10**9+7

def COM(n,r):
    P,Q=1,1
    for i in range(r):
        P=P*(n-i)%MOD
        Q=Q*(r-i)%MOD
    return P*pow(Q,MOD-2,MOD)%MOD

N,M=map(int,input().split())
S=sum(list(map(int,input().split())))

print(COM(N+M,S+N))
