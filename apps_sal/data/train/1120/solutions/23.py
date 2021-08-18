for _ in range(int(input())):
    r, c = map(int, input().split())
    r = r - 1
    c = c - 1
    max = -1 * 10**9
    x, y = map(int, input().split())
    xx = [0, r, 0, r]
    yy = [0, 0, c, c]
    for i in range(4):
        d = abs(x - xx[i]) + abs(y - yy[i])
        if d > max:
            max = d
    print(max)
