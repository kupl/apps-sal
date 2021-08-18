
for _ in range(int(input())):
    n = int(input())
    l = []
    for i in range(n):
        a = input()
        l.append(a)
    x = 0
    y = 0
    p = 0
    q = 0
    li = []
    for i in range(n):
        p = 0
        q = 0
        for j in range(n):
            if j < (n / 2) and l[i][j] == "1":
                x += 1
                p += 1
            elif j >= (n / 2) and l[i][j] == "1":
                y += 1
                q += 1
        a = []
        a = (p, q)
        li.append(a)
    mi = abs(x - y)
    if x - y == 0:
        print(x - y)
    else:
        mi = abs(x - y)
        d = x - y
        for i in range(n):
            c = x - li[i][0] + li[i][1]
            b = y + li[i][0] - li[i][1]
            z = abs(c - b)
            if mi > abs(z):
                mi = abs(z)
        print(mi)
