MOD = 10**9 + 7
def I(): return list(map(int, input().split()))


t, = I()
while t:
    t -= 1
    n, m = I()
    l = []
    i = 1
    while (i * m) % 10 not in l:
        l.append((i * m) % 10)
        i += 1
    k = len(l) * m
    ans = sum(l) * (n // k)
    i = n // k * k
    j = 1
    while i + j * m <= n:
        ans += (i + j * m) % 10
        j += 1
    print(ans)
