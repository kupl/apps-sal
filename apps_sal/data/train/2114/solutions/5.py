def R():
    return map(int, input().split())


ans = 0
(n, m) = R()
F = list(R())
for i in range(m):
    (a, b, x) = R()
    ans = max(ans, (F[a - 1] + F[b - 1]) / x)
print(ans)
