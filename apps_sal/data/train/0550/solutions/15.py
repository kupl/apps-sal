t = int(input())
while(t):
    t -= 1
    a, b = list(map(int, input().split()))
    a = bin(a).replace("0b", "")
    b = bin(b).replace("0b", "")
    s1 = len(a)
    s2 = len(b)
    if(s1 != s2):
        if(s1 > s2):
            f = s1 - s2
            b = (f * '0') + b
        else:
            f = s2 - s1
            a = (f * '0') + a
    s1 = len(a)
    s2 = len(b)
    t1 = b.count('1')
    t2 = b.count('0')
    if(s2 == t1 or s2 == t2):
        n = int(a) ^ int(b)
        m = int(str(n), 2)
        print(0, m)
    else:
        v = []
        g = int(a, 2)
        h = int(b, 2)
        j = g ^ h
        v.append(j)
        for i in range(1, len(b)):
            b = b[-1] + b[0:-1]
            c = int(b, 2)
            v.append(g ^ c)
        y = max(v)
        print(v.index(y), y)
