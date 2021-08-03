t = int(input())
while t:
    t = t - 1
    n = int(input())
    b = list(map(int, input().split()))
    g = list(map(int, input().split()))
    a = []
    b.sort()
    g.sort()
    for i in range(n):
        a.append(b[i])
        a.append(g[i])
    c = []
    for i in range(n):
        c.append(g[i])
        c.append(b[i])
    f, f1 = 0, 0
    for i in range(2 * n - 1):
        if(a[i] > a[i + 1]):
            f = 1
            break
    for i in range(2 * n - 1):
        if(c[i] > c[i + 1]):
            f1 = 1
            break
    if(f == 0 or f1 == 0):
        print("YES")
    else:
        print("NO")
