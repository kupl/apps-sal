try:
    testcases = int(input())
    for i in range(testcases):
        rects = int(input())
        xCords = {}
        yCords = {}

        def check(x, hashMap):
            return True if x in hashMap else False
        for i in range(rects * 4 - 1):
            (x, y) = list(map(int, input().split()))
            xCords[x] = xCords.get(x, 0) + 1
            yCords[y] = yCords.get(y, 0) + 1
        for ((i, j), (i1, j1)) in zip(xCords.items(), yCords.items()):
            if j % 2 != 0:
                x = i
            if j1 % 2 != 0:
                y = i1
        print(x, y)
except:
    pass
