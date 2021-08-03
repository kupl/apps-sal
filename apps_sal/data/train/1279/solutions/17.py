for T in range(int(input())):

    N = int(input())

    d = dict()
    for i in range(N):
        x, y = list(map(int, input().split()))

        f = d.get(x)

        if f == None:
            d[x] = y
        else:
            d[x] = max(f, y)

    l = len(d)

    if l < 3:
        print(0)
    else:
        Y = sorted(list(d.items()), key=lambda x: x[1])
        print(Y[l - 1][1] + Y[l - 2][1] + Y[l - 3][1])
