M = 10 ** 9 + 7
for _ in range(int(input())):
    s,p,m,r = list(map(int, input())),0,1,0
    for d in reversed(s):
        p += d * m
        m = m * 10 % M
    for d in s:
        r = (r * m + p) % M
        p = (p * 10 - (m - 1) * d) % M
    print(r)
