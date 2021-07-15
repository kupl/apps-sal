N, M = map(int, input().split())
s = sum(list(map(int, input().split())))

p = 10 ** 9 + 7

fact = [1, 1]
factinv = [1, 1]
inv = [0, 1]

for i in range(2, s + N + 1):
    fact.append((fact[-1] * i) % p)
    inv.append((-inv[p % i] * (p // i)) % p)
    factinv.append((factinv[-1] * inv[-1]) % p)

ans = factinv[s + N]

for i in range(s + N):
    ans *= M + N - i
    ans %= p

print(ans)
