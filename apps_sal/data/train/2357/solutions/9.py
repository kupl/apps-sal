n, m = map(int, input().split())
a = list(map(int, input().split()))
s = sum(a)
mod = 10 ** 9 + 7
ans, cnt = 1, 1
for i in range(n + m, m - s, -1):
    ans *= i
    ans %= mod
for i in range(1, s + n + 1):
    cnt *= i
    cnt %= mod
print(ans * pow(cnt, mod - 2, mod) % mod)
