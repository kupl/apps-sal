
t = int(input())
for _ in range(t):
    q = int(input())
    s = []
    e, o = 0, 0
    for __ in range(q):
        x = int(input())
        d = []
        if x not in s:
            for i in s:
                xo = i ^ x
                d.append(xo)
            d = set(d)
            for i in d:
                if i not in s:
                    if bin(i).count('1') % 2 == 0:
                        e += 1
                    else:
                        o += 1
            s.append(x)
            if bin(x).count('1') % 2 == 0:
                e += 1
            else:
                o += 1
            for i in d:
                s.append(i)
        print(e, o)
