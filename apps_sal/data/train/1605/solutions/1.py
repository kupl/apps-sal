
(a, b) = list(map(int, input().split()))


ans = a * (a + 1) * b * b * (b - 1)
ans //= 4
ans += a * b * (b - 1) // 2

MOD = 1000000007
ans %= MOD

print(ans)
