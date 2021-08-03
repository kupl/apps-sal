n, m = map(int, input().split())
a = list(map(int, input().split()))
mod = 10**9 + 7
inv = [0, 1]
for i in range(2, 5 * 10**6):
    inv += [inv[mod % i] * (mod - int(mod / i)) % mod]
s = sum(a)
ans = 1
for i in range(n + s):
    ans *= (n + m - i)
    ans %= mod
    ans *= inv[i + 1]
    ans %= mod
print(ans)
