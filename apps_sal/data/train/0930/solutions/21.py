t = int(input())
while t > 0:
    n = int(input())
    l = []
    for i in range(n):
        l1 = []
        for j in range(n):
            l1.append(0)
        l.append(l1)
    c = 1
    for j in range(n):
        k = 0
        for i in range(j, -1, -1):
            l[k][i] = c
            c += 1
            k += 1
    for i in range(1, n):
        m = i
        for j in range(n - i):
            l[m][n - j - 1] = c
            c += 1
            m += 1
    for p in l:
        print(*p)

    t -= 1
