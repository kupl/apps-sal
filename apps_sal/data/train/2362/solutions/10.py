q = int(input())
for i in range(q):
    n = int(input())
    rowdown = -10 ** 5
    rowup = 10 ** 5
    colmnleft = -10 ** 5
    colmnright = 10 ** 5
    for j in range(n):
        x, y, left, up, right, down = list(map(int, input().split()))
        if not left:
            colmnleft = max(colmnleft, x)
        if not right:
            colmnright = min(colmnright, x)
        if not up:
            rowup = min(rowup, y)
        if not down:
            rowdown = max(rowdown, y)
    if rowdown > rowup or colmnleft > colmnright:
        print(0)
    else:
        print(1, colmnleft, rowdown)
