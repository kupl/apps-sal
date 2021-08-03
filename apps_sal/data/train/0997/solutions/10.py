try:
    t = int(input())
    for a in range(t):
        l = input().split()
        n = int(l[0])
        m = int(l[1])
        d = {}
        s = 0
        for b in range(m):
            l1 = input().split()
            i = int(l1[0])
            j = int(l1[1])
            k = int(l1[2])
            for c in range(i, j + 1):
                if c not in d:
                    d[c] = 10
            for c in range(i, j + 1):
                d[c] = d[c] * k
        for i in d:
            s = s + d[i]
        print(s // n)
except:
    pass
