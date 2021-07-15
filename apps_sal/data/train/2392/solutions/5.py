for TT in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    x = (n // m) + 1
    l = [0]
    while True:
        d = (l[-1] + m) % 10
        if d in l: break
        l.append(d)
    n = len(l)
    a, b = x // n, x % n
    print(sum(l) * a + sum(l[:b]))
