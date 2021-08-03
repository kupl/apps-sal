mod = 10**9 + 7
n, m = map(int, input().split())
s = sum(map(int, input().split()))
a = n + m
b = s + n
num = 1
den = 1
for i in range(b):
    num *= a - i
    num %= mod
    den *= i + 1
    den %= mod
ans = num * pow(den, mod - 2, mod) % mod
print(ans)
