t = int(input())
while t:
    l = input().split()
    a = int(l[0])
    b = int(l[1])
    a = str(bin(a).replace('0b', ''))
    b = str(bin(b).replace('0b', ''))
    if len(a) != len(b):
        if len(a) > len(b):
            m = len(a) - len(b)
            b = '0' * m + b
        else:
            m = len(b) - len(a)
            a = '0' * m + a
    l = len(b)
    s1 = b.count('1')
    s2 = b.count('0')
    if l == s1 or l == s2:
        j = int(a) ^ int(b)
        k = int(str(j), 2)
        print(0, k)
    else:
        l1 = []
        o = int(a, 2)
        p = int(b, 2)
        q = o ^ p
        l1.append(q)
        for i in range(1, l):
            b = b[-1] + b[0:-1]
            c = int(b, 2)
            l1.append(o ^ c)
        maxx = max(l1)
        print(l1.index(maxx), maxx)
    t -= 1
