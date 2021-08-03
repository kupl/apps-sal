def gta(limit, *args):
    ns = []
    for i in args:
        a = list(str(i))
        a.reverse()
        ns.append(a)

    base_list = []
    while ns and len(base_list) < limit:
        n = ns.pop(0)
        if n:
            b = int(n.pop())
            if b not in base_list:
                base_list.append(b)
            if n:
                ns.append(n)

    base = sum(base_list)
    times = 0
    for i in range(1, 1 + limit):
        t = i
        for j in range(i - 1):
            t *= limit - j - 1
        times += t
    return base * times
