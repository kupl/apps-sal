try:
    cnt = 0
    l = []
    d = {}
    t = tuple()
    for _ in range(int(input())):
        w = [int(i) for i in input().split()]
        w.sort()
        l.append(w)
    t = tuple(l)
    for i in t:
        if tuple(i) not in d:
            d[tuple(i)] = 1
        else:
            d[tuple(i)] += 1
    for i in d:
        if d[i] == 1:
            cnt += 1
    print(cnt)
except EOFError as e:
    pass
