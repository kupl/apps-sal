for _ in range(int(input())):
    t = int(input())
    s = input()
    b = []
    a = []
    c = 0
    lb = 0
    la = 0
    r = []
    ls = len(s)
    for i in (s):
        c += 1
        if i == 'B':
            lb += 1
        else:
            la += 1
    if (la - lb) == 0 or abs(la - lb) == 1:
        if la < lb:
            for i in range(ls):
                if i % 2 == 1 and s[i] == 'B':
                    b.append(i)
                if i % 2 == 0 and s[i] == 'G':
                    a.append(i)
        elif la > lb:
            for i in range(ls):
                if i % 2 == 0 and s[i] == 'B':
                    b.append(i)
                if i % 2 == 1 and s[i] == 'G':
                    a.append(i)
        cs = 0
        sw = 0
        for i in range(len(a)):
            cs += abs(a[i] - b[i])
        if t == 0:
            cs = len(a)
        if la == lb:
            for i in range(len(s)):
                if i % 2 == 0 and s[i] == 'B':
                    b.append(i)
                if i % 2 == 1 and s[i] == 'G':
                    a.append(i)
            cs = 0
            sw = 0
            for i in range(len(a)):
                cs += abs(a[i] - b[i])
            if t == 0:
                cs = len(a)
            x = cs
            b = []
            a = []
            for i in range(len(s)):
                if i % 2 == 1 and s[i] == 'B':
                    b.append(i)
                if i % 2 == 0 and s[i] == 'G':
                    a.append(i)
            cs = 0
            sw = 0
            for i in range(len(a)):
                if i < len(b):
                    cs += abs(a[i] - b[i])
            if t == 0:
                cs = len(a)
            cs = min(x, cs)
        print(cs)
    else:
        print(-1)
