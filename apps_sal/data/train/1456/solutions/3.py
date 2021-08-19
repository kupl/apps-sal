def fun(m):
    sumi = m * (m + 1) // 2
    f = 1
    while f <= m:
        x = m // f + 1
        sumi -= 1 + f * (x // 2)
        f *= 2
    return sumi


t = int(input())
for _ in range(t):
    (l, r) = map(int, input().split())
    print(fun(r) - fun(l - 1))
