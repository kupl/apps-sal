for t in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    D = {}
    for i in l:
        if i in D:
            D[i] += 1
        else:
            D[i] = 1
    d = {1: 0, 2: 0, 3: 0}
    for i in list(D.values()):
        if i == 1:
            d[1] += 1
        elif i % 2 == 0:
            d[2] += 1
        else:
            d[3] += 1
    c = 0
    for i in d:
        if i == 1:
            c = c + d[i]
        elif i == 2:
            if d[2] % 2 == 0:
                c = c + d[2]
            else:
                c = c + d[2] - 1
        else:
            c = c + d[3]
    print(c)
