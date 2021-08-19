# cook your dish here
t = int(input())
for i in range(t):
    n = int(input())
    a = [0]
    b = [0]
    c = [0]
    d = [0]
    e = [0]
    f = [0]
    g = [0]
    h = [0]
    for j in range(n):
        q, s = list(map(int, input().split()))
        if q < 9:
            if q == 1:
                a.append(s)
            elif q == 2:
                b.append(s)
            elif q == 3:
                c.append(s)
            elif q == 4:
                d.append(s)
            elif q == 5:
                e.append(s)
            elif q == 6:
                f.append(s)
            elif q == 7:
                g.append(s)
            elif q == 8:
                h.append(s)
    print(max(a) + max(b) + max(c) + max(d) + max(e) + max(f) + max(g) + max(h))
