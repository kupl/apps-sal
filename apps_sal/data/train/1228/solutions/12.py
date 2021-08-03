T = int(input())
for i in range(T):
    N = int(input())
    xcord = {}
    ycord = {}
    for i in range(4 * N - 1):
        x, y = list(map(int, input().split()))
        xcord[x] = xcord.get(x, 0) + 1
        ycord[y] = ycord.get(y, 0) + 1
    x = None
    y = None

    for i in xcord:
        if xcord[i] % 2 != 0:
            x = i
            break
    for i in ycord:
        if ycord[i] % 2 != 0:
            y = i
            break
    print(x, y)
