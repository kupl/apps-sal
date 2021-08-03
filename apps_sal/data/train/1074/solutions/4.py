# cook your dish here
t = int(input())
for i in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    s = set(l)
    d = []
    d1 = []
    h = 0
    for j in s:
        d.append(l.count(j))
    d2 = list(set(d))
    d2.sort(reverse=True)
    for v in d2:
        if (v > 1) and (v % 2 == 0):
            d1.append(v)
    for k in d1:
        q = k // 2
        if (d.count(k) == 2):
            h = h + q
        elif q >= 2:
            h = h + (q // 2)

    if h == 0:
        print(0)
    else:
        print(h)
