N, M = map(int, input().split())
A = list(map(int, input().split()))
sa = sum(A)
MOD = 10**9 + 7
if sa > M:
    print(0)
    return
if sa == M:
    print(1)
    return

x = 1 + sa + N
n = M - sa

bunsi = bunbo = 1
for i in range(max(x, n + 1), x + n):
    bunsi *= i
    bunsi %= MOD

for i in range(1, min(x, n + 1)):
    bunbo *= i
    bunbo %= MOD

ans = bunsi * pow(bunbo, MOD - 2, MOD)
ans %= MOD
print(ans)
