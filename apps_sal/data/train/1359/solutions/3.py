for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    ev = []
    od = []

    for i in a:
        if i % 2 == 0:
            ev.append(i)
        else:
            od.append(i)
    c = 0
    c1 = 0
    cc = 0
    cc1 = 0
    if od:
        mo = max(od)
        for i in a:
            if i != mo and i % 2 != mo % 2:
                c += 1
            elif i != mo and i % 2 == mo % 2:
                c += 2
        mo += 1
        for i in a:
            if i % 2 == mo % 2:
                cc += 2
            else:
                cc += 1

    if ev:
        me = max(ev)
        for i in a:
            if i != me and i % 2 == me % 2:
                c1 += 2
            elif i != me and i % 2 != me % 2:
                c1 += 1
        me += 1
        for i in a:
            if i % 2 == me % 2:
                cc1 += 2
            else:
                cc1 += 1
    if ev and od:
        print(min(c, c1, cc, cc1))
    elif not ev:
        print(min(cc, c))
    elif not od:
        print(min(cc1, c1))
