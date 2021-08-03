q = int(input())
for _ in range(q):
    n = int(input())
    x = []
    y = []
    f = []
    for _ in range(n):
        temp = tuple(map(int, input().split()))
        x.append(temp[0])
        y.append(temp[1])
        f.append(temp[2:])
    x_min = y_min = -100000
    x_max = y_max = 100000
    for i in range(n):
        if f[i][0] == 0:
            x_min = max(x_min, x[i])
        if f[i][1] == 0:
            y_max = min(y_max, y[i])
        if f[i][2] == 0:
            x_max = min(x_max, x[i])
        if f[i][3] == 0:
            y_min = max(y_min, y[i])
    if x_max < x_min:
        print(0)
        continue
    elif y_max < y_min:
        print(0)
        continue
    else:
        print('1 %d %d' % (x_min, y_min))
