for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    d = {}
    for i in l:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    nd = {1: 0, 2: 0, 3: 0}
    for i in list(d.values()):
        if i == 1:
            nd[1] += 1
        elif i % 2 == 0:
            nd[2] += 1
        else:
            nd[3] += 1
    c = 0
    for i in nd:
        if i == 1:
            c = c + nd[i]
        elif i == 2:
            if nd[2] % 2 == 0:
                c = c + nd[2]
            else:
                c = c + nd[2] - 1
        else:
            c = c + nd[3]
    print(c)
