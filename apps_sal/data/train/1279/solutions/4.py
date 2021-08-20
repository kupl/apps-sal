def optimize(d):
    l = list(d.keys())
    if len(l) < 3:
        return 0
    else:
        j = []
        for i in l:
            j.append(d[i])
        j.sort()
        return j[len(j) - 1] + j[len(j) - 2] + j[len(j) - 3]


try:
    for _ in range(int(input())):
        (x, y, d) = ([], [], {})
        for i in range(int(input())):
            j = list(map(int, input().strip().split()))
            x.append(j[0])
            y.append(j[1])
            if x[i] not in d:
                d[x[i]] = y[i]
            else:
                d[x[i]] = max(y[i], d[x[i]])
        print(optimize(d))
except EOFError as e:
    pass
