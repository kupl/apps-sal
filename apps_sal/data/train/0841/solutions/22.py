M = 10 ** 9 + 7

t = int(input())
for _ in range(t):
    s = list(map(int, input()))
    p, m = 0, 1
    for d in reversed(s):
        p += d * m
        m = m * 10 % M
    r = 0
    for d in s:
        r = (r * m + p) % M
        p = (p * 10 - (m - 1) * d) % M
    print(r)

