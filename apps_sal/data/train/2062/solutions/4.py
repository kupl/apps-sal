mod = 10**9+7
def inpl(): return [int(i) for i in input().split()]
N, A, B, C, D = inpl()
fac = [1 for _ in range(N+1)]
for i in range(N):
    fac[i+1] = (i+1)*fac[i] %mod
inv = [1 for _ in range(N+1)]
for i in range(2,N+1):
    inv[i] = (-(mod//i) * inv[mod%i]) %mod    
facinv = [1 for _ in range(N+1)]
for i in range(N):
    facinv[i+1] = inv[i+1]*facinv[i] %mod
facinvp = [facinv]
for i in range(N-1):
    p = facinvp[-1]
    q = [p[i]*facinv[i]%mod for i in range(N+1)]
    facinvp.append(q)
    
dp = [[0 for _ in range(N+1)] for _ in range(B+1)]
dp[A-1][0] = 1

for i in range(A-1,B):
    for j in range(N+1):
        dp[i+1][j] = dp[i][j]
        for k in range(C,1+min(D, j//(i+1))):
            x = j - k*(i+1)
            dp[i+1][j] += fac[j]*facinv[x]*facinvp[k-1][i+1]*facinv[k]*dp[i][x]%mod
        dp[i+1][j] %= mod
print(dp[B][N])
