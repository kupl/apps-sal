for t in range(int(input())):
    N = list(map(int, input().split()))
    c = 0
    p = 0
    l = []
    l1 = []
    for i in N:
        p += 1
        if i > 30:
            c += 1
        if i > 0:
            if i % 2 == 0:
                l.append(i * p)
                l1.append(p)
    out = sum(l) / sum(l1)
    print('{} {:.2f}'.format(c, out))
