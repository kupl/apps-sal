import bisect as b
t = int(input())
while t:
    t -= 1
    (n, k) = map(int, input().split())
    a = list(map(int, input().split()))
    c = 0
    for i in range(n):
        x = [0]
        d = dict()
        for j in range(i, n):
            b.insort(x, a[j])
            y = k / (len(x) - 1)
            if d.get(a[j], -1) == -1:
                d[a[j]] = 1
            else:
                d[a[j]] += 1
            if int(y) != y:
                y = int(y) + 1
            y = int(y)
            z = k / y
            if int(z) != z:
                z = int(z) + 1
            z = int(z)
            q = d[x[z]]
            if d.get(q, -1) != -1:
                c += 1
    print(c)
