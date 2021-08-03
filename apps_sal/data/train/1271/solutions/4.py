import collections
t = int(input())
for _ in range(t):
    q = int(input())
    s = collections.defaultdict(lambda: -1)
    e, o = 0, 0
    for __ in range(q):
        x = int(input())
        d = []
        # print(s)
        dd = list(s)
        if s[x] == -1:
            for i in dd:
                xo = i ^ x
                d.append(xo)
            d = set(d)
            for i in d:
                if s[i] == -1:
                    if bin(i).count('1') % 2 == 0:
                        e += 1
                    else:
                        o += 1
                    s[i] = 1
            s[x] = 1
            if bin(x).count('1') % 2 == 0:
                e += 1
            else:
                o += 1
            for i in d:
                s[i] = 1
        print(e, o)
