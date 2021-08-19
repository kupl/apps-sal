import math
for _ in range(int(input())):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    count = 0
    # y=a.copy()
    # y.sort()
    y = dict()
    for i in range(n):
        if y.get(a[i]):
            y[a[i]] += 1
        else:
            y[a[i]] = 1
    for i in range(n):
        if a[i] >= x:
            pass
        else:
            p = x - a[i]
            if y.get(p):
                count += y[p]
            else:
                pass
    p = math.sqrt(x)
    if n < p:
        p = n
    b = []
    k = 2
    while k <= p:
        if x % k == 0:
            b.append(k)
        k += 1
    # print(b)
    for i in b:
        summ = 0
        for j in range(i):
            summ += a[j]
        c = [summ]
        p = 0
        for j in range(i, n):
            summ += a[j]
            summ -= a[p]
            p += 1
            c.append(summ)
        # c.sort()
        l = len(c)
        # print(i)
        # print(c)
        y = dict()
        for j in range(l):
            if y.get(c[j]):
                y[c[j]] += 1
            else:
                y[c[j]] = 1
        for j in range(l):
            if c[j] >= (x // i):
                pass
            else:
                p = (x // i) - c[j]
                if y.get(p):
                    count += y[p]
                else:
                    pass

    print(count)
