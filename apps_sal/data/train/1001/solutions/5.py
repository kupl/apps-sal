def prices(n, p):
    c = 0
    for i in range(n):
        if i == 0:
            c += 1
        elif i < 6:
            if p[i] < min(p[:i]):
                c += 1
        elif p[i] < min(p[i - 5:i]):
            c += 1
    return c


t = int(input())
for i in range(t):
    n = int(input())
    p = list(map(int, input().split()))
    print(prices(n, p))
