t = eval(input())
while t != 0:
    n = eval(input())
    x = []
    y = []
    for i in range(0, n):
        b = list(map(int, input().split(' ')))
        x.append(b[1])
        y.append(b[0])
    xy = list(zip(*sorted(zip(x, y))))
    x = xy[0]
    y = xy[1]
    for i in reversed(list(range(0, n))):
        if x[i] != 0:
            if i != n - 1:
                print('+', end=' ')
            if x[i] == 1:
                print('%d' % (x[i] * y[i]), end=' ')
            else:
                print('%dx^%d' % (x[i] * y[i], x[i] - 1), end=' ')
    print()
    t = t - 1
