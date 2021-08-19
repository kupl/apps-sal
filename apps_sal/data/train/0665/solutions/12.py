for _ in range(int(input())):
    (n, m) = map(int, input().split())
    r = list(map(int, input().split()))
    a = []
    for i in range(n):
        b = list(map(int, input().split()))
        count = r[i]
        for j in range(m):
            count += b[j]
            b[j] = count
        a.append(b)
    b = []
    p = 0
    for i in range(n):
        p = [0] * m
        b.append(p)
    for i in range(m):
        c = []
        for j in range(n):
            c.append(a[j][i])
        c.sort(reverse=True)
        for j in range(n):
            b[j][i] = c.index(a[j][i])
    count = 0
    for i in range(n):
        p = a[i].index(max(a[i]))
        q = b[i].index(min(b[i]))
        if p != q:
            count += 1
    print(count)
