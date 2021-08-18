t = int(input())
l = []
for i in range(0, t):
    ele = list(map(int, input().split()))
    l.append(ele)
for i in range(0, t):
    n = l[i][0]
    m = l[i][1]
    f1 = []
    f2 = []
    for j in range(1, n + 1):
        for h in range(1, m + 1):
            f1.append((j, h))
    for j in range(1, m + 1):
        for h in range(1, n + 1):
            f2.append((h, j))

    for k in range(0, n * m):
        if k == 0:
            print(n * m, end=' ')
        else:
            y = []
            z = []
            e = 0
            while e * (k + 1) < n * m:

                y.append(f1[e * (k + 1)])
                z.append(f2[e * (k + 1)])
                e = e + 1

            for x in z:
                if x not in y:
                    y.append(x)

            print(len(y), end=' ')
