try:
    testcases = int(input())
    for i in range(testcases):
        rects = int(input())
        xCords = {}
        yCords = {}
        for i in range(rects * 4 - 1):
            (x, y) = list(map(int, input().split()))
            xCords[x] = xCords.get(x, 0) + 1
            yCords[y] = yCords.get(y, 0) + 1
        x = None
        y = None
        for i in xCords:
            if xCords[i] % 2 != 0:
                x = i
                break
        for i in yCords:
            if yCords[i] % 2 != 0:
                y = i
                break
        print(x, y)
except:
    pass
