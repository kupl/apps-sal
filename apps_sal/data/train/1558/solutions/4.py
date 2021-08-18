from math import ceil
for _ in range(int(input())):
    n, m = list(map(int, input().split()))
    l = [str(n * m)]
    for i in range(1, n * m):
        c = 2 * ceil((n * m) / (i + 1))
        for k in range(0, n * m, i + 1):
            r = k % m
            q = k // m
            if((r * n + q) % (i + 1) == 0):
                c -= 1
        l.append(str(c))
    print(" ".join(l))
