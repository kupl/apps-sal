t = int(input())
for _ in range(t):
    (n, q) = list(map(int, input().split()))
    v = list(map(int, input().split()))
    vv = v[:]
    vv = [[j, i] for (j, i) in enumerate(v)]
    vv.sort(key=lambda x: x[1])
    vvv = []
    for (jj, i) in enumerate(vv):
        v[i[0]] = [jj, i[1]]
    for i in range(q):
        (x, y) = list(map(int, input().split()))
        x -= 1
        y -= 1
        xx = v[x][0]
        yy = v[y][0]
        if xx < yy:
            le = yy - xx + 1
            cost = v[y][1] - v[x][1]
            cost += y - x
        elif xx == yy:
            le = 1
            cost = 0
        else:
            le = xx - yy + 1
            cost = v[x][1] - v[y][1]
            cost -= x - y
        print(cost, le)
