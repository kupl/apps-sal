t = int(input())
for i in range(t):
    n = int(input())
    if n < 101:
        l1 = []
        l2 = []
        d = dict()
        for i in range(1, 2 * n + 1):
            if i % 2 == 0:
                l1.append(int(input()))
            else:
                l2.append(str(input()))
        r1 = []
        for i in l1:
            r1.append(i)
        l1.sort()
        ind = []
        for i in l1:
            a = r1.index(i)
            ind.append(a)
        for i in ind:
            print(l2[i])
    else:
        break
