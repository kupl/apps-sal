# cook your dish here
def fun(st, en, l):
    for i in range(st, maxpow + 1):
        for j in range(0, m - 1):
            l[i][j] = l[i - 1][0] * l[i - 2][j + 1] - l[i - 2][0] * l[i - 1][j + 1]


for _ in range(int(input())):
    l = list(map(int, input().split()))
    n = len(l)
    el = []
    ol = []
    for i in range(n):
        if i % 2 == 0:
            el.append(l[i])
        else:
            ol.append(l[i])
    if n % 2 != 0:
        ol.append(0)
    l = []
    l.append(el)
    l.append(ol)
    m = len(el)
    maxpow = n - 1
    for i in range(2, maxpow + 1):
        l.append([0] * m)
    fun(2, maxpow + 1, l)
    for i in range(maxpow + 1):
        cze = 0
        for j in range(m):
            if l[i][j] == 0:
                cze += 1
        if cze == m:
            for k in range(m):
                l[i][k] = l[i - 1][k] * maxpow + 4 - (i + 1) - 2 * (k + 1)
            fun(i + 1, maxpow + 1, l)
    check = 0
    for i in range(maxpow + 1):
        if l[i][0] == 0 and sum(l[i][1:]) != 0:
            print(0)
            check = 1
            break
    if check == 0:
        if l[0][0] > 0:
            signchange = 1
        else:
            signchange = -1
        c = 0
        for i in range(maxpow + 1):
            if l[i][0] > 0:
                temp = 1
            else:
                temp = -1
            if temp != signchange:
                print(0)
                c = 1
                break
        if c == 0:
            print(1)
