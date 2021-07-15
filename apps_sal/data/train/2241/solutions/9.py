N, C = list(map(int,input().split()))
A = list(map(int,input().split()))
B = list(map(int,input().split()))
MOD = 10**9 + 7
MB = max(B)

Sm = [[1 for _ in range(MB+1)]]
for c in range(1,C+1):
  Sm.append([])
  s = Sm[-1]
  sp = Sm[-2]
  for i in range(MB+1):
    s.append((i*sp[i]) % MOD)
    
for c in range(C+1):
  s = Sm[c]
  for i in range(1,MB+1):
    s[i] += s[i-1]
    s[i] %= MOD
    
DP = [[0 for _ in range(C+1)] for _ in range(N+1)]
DP[0][0] = 1
for n in range(1,N+1):
  dp = DP[n]
  dpp = DP[n-1]
  for c in range(C+1):
    for cc in range(C+1-c):
      dp[c+cc] += dpp[c] * (Sm[cc][B[n-1]] - Sm[cc][A[n-1]-1])
      dp[c+cc] %= MOD
print((DP[N][C] % MOD))
    

