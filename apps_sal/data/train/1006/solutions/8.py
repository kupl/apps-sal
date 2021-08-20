t = int(input())
for _ in range(t):
    (n, k) = list(map(int, input().split()))
    s = list(str(n))
    l = len(s)
    s1 = ''
    if int(min(s)) > k:
        for i in range(l):
            s1 += str(k)
        print(s1)
    else:
        c = min(s)
        while int(c) != k and len(s) != 0:
            s1 += c
            ind = s.index(c)
            s = s[ind + 1:]
            for i in range(ind + 1):
                s.append(str(k))
            c = min(s)
        z = len(s1)
        for i in range(l - z):
            s1 += str(k)
        print(s1)
