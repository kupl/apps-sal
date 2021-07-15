MOD = 10**9 + 7

fact = [1 for i in range(101)]
for i in range(2, 100):
 fact[i] = (fact[i - 1] * i) % MOD

inv = [1 for i in range(101)]
for i in range(0, 100):
 inv[i] = pow(fact[i], MOD - 2, MOD)

def C(n, r):
 return (((fact[n] * inv[r]) % MOD) * inv[n - r]) % MOD

t = int(input())
for qq in range(t):
 n, k = list(map(int, input().split()))
 for kk in range(n - 1):
  a, b = list(map(int, input().split()))

 ans = 0
 for i in range(1, k + 1):
  if (i-1) > (n-1):
   break
  cur = C(n - 1, i - 1) * C(k, i)
  cur %= MOD
  cur *= fact[i]
  cur %= MOD
  ans += cur
  ans %= MOD

 print(ans % MOD)

