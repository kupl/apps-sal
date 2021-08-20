mod = 998244353
n = int(input())
deg = [0] * (n + 1)
fac = [1] * (n + 1)
for i in range(1, n + 1):
    fac[i] = fac[i - 1] * i % mod
for i in range(n - 1):
    (a, b) = list(map(int, input().split()))
    deg[a] += 1
    deg[b] += 1
s = 1
for i in range(1, n + 1):
    s = s * fac[deg[i]] % mod
s = s * n % mod
print(s)
