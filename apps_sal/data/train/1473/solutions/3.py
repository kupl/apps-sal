for t in range(int(input())):
    r, c, p1, p2, p3 = list(map(int, input().split()))
    if ((r * c) != (p1 + p2 + p3)):
        print('No')
        continue
    if (p1 % r) == 0:
        nc = c - (p1 / r)
        if ((p2 % r == 0 and p3 % r == 0) or (p2 % nc == 0 and p3 % nc == 0)):
            print('Yes')
            continue
    if (p2 % r) == 0:
        nc = c - (p2 / r)
        if ((p1 % r == 0 and p3 % r == 0) or (p1 % nc == 0 and p3 % nc == 0)):
            print('Yes')
            continue
    if (p3 % r) == 0:
        nc = c - (p3 / r)
        if ((p2 % r == 0 and p1 % r == 0) or (p2 % nc == 0 and p1 % nc == 0)):
            print('Yes')
            continue
    if (p1 % c) == 0:
        nr = r - (p1 / c)
        if ((p2 % nr == 0 and p3 % nr == 0) or (p2 % c == 0 and p3 % c == 0)):
            print('Yes')
            continue
    if (p2 % c) == 0:
        nr = r - (p2 / c)
        if ((p1 % nr == 0 and p3 % nr == 0) or (p1 % c == 0 and p3 % c == 0)):
            print('Yes')
            continue
    if (p3 % c) == 0:
        nr = r - (p3 / c)
        if ((p2 % nr == 0 and p1 % nr == 0) or (p2 % c == 0 and p1 % c == 0)):
            print('Yes')
            continue
    print('No')
