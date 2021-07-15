MOD = 998244353


def f(N, K):
    if K > N:
        return 0
    
    S0 = [1]
    for i in range(1, N+1):
        S1 = [0]*(i+1)
        for j in range(i, 0, -1):
            S1[j] = (S0[j-1] + (S1[j*2] if j*2<=i else 0))%MOD
        S0 = S1
    
    return S0[K]
        
N, K = list(map(int, input().split()))
print((f(N,K)))

