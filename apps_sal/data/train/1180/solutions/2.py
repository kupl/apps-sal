a = int(input())
t = []
for _ in range(a):
    (n, k, x, y) = list(map(int, input().split()))
    l = [(0, 0), (n, 0), (0, n), (n, n)]
    d = {
    }
    tt = 1
    m = 0
    while(tt):
        if(x > y):
            b, c = n, y + n - x
            d[1] = (b, c)
            if((b, c) in l):
                t.append((b, c))
                m = 1
                break
            d[2] = (c, b)
            if((c, b) in l):
                t.append((c, b))
                m = 1
                break
            b, c = 0, x - y
            d[3] = (b, c)
            if((b, c) in l):
                t.append((b, c))
                m = 1
                break
            d[0] = (c, b)
            if((c, b) in l):
                t.append((c, b))
                m = 1
                break
            tt = 0
        else:
            c, b = n, x + n - y
            d[1] = (b, c)
            if((b, c) in l):
                t.append((b, c))
                m = 1
                break
            d[2] = (c, b)
            if((c, b) in l):
                t.append((c, b))
                m = 1
                break
            c, b = 0, y - x
            d[3] = (b, c)
            if((b, c) in l):
                t.append((b, c))
                m = 1
                break
            d[0] = (c, b)
            if((c, b) in l):
                t.append((c, b))
                m = 1
                break
            tt = 0

    if(m == 0):
        t.append(d[k % 4])
for i in t:
    print(*i)
