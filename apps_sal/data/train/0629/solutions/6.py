t = int(input())
while t > 0:
    (r, g, q, m) = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    for i in range(m):
        x = max(a)
        y = max(b)
        z = max(c)
        if x >= y and x >= z:
            for j in range(r):
                a[j] //= 2
        elif y >= x and y >= z:
            for j in range(g):
                b[j] //= 2
        else:
            for j in range(q):
                c[j] //= 2
    x = max(a)
    y = max(b)
    z = max(c)
    print(max(x, max(y, z)))
    t -= 1
