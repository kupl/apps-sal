for _ in range(int(input())):
    n = int(input())
    d = {}
    for i in range(n):
        (x, y) = list(map(int, input().split()))
        if x not in d:
            d[x] = []
            d[x].append(y)
        else:
            d[x][0] = max(d[x][0], y)
    y = []
    for v in d:
        y.extend(d[v])
    if len(y) >= 3:
        v1 = max(y)
        y.remove(v1)
        v2 = max(y)
        y.remove(v2)
        v3 = max(y)
        y.remove(v3)
        print(v1 + v2 + v3)
    else:
        print(0)
