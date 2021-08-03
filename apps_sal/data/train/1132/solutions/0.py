mod = 1000000007
fac = [1, 1]
maxn = (10**5) + 5
for i in range(2, maxn):
    x = (fac[-1] * i) % mod
    fac.append(x)

pre = [1]
for i in range(2, maxn):
    x = 2 * i - 1
    x = (pre[-1] * x) % mod
    pre.append(x)

for _ in range(int(input())):
    n = int(input())
    x = fac[n]
    y = pre[n - 1]
    print((x * y) % mod)
