from collections import defaultdict
T = int(input())
for _ in range(T):
    ax, ay, bx, by, cx, cy = list(map(int, input().split()))
    X = defaultdict(int)
    Y = defaultdict(int)
    X[ax] += 1
    X[bx] += 1
    X[cx] += 1
    Y[ay] += 1
    Y[by] += 1
    Y[cy] += 1
    x = min(X)
    y = min(Y)
    r = None
    if X[x] == 1 and Y[y] == 1:
        r = 0
    elif X[x] == 1 and Y[y] == 2:
        r = 3
    elif X[x] == 2 and Y[y] == 1:
        r = 1
    else:
        r = 2
    if r == 0:
        ans = max(abs(2 * x + 1), abs(2 * y + 1))
        if x == y and x != 0:
            ans += 1
        print(ans)
    elif r == 1:
        t = None
        ans = None
        if y >= 0:
            t = abs(y) - abs(x)
        else:
            t = abs(y + 1) - abs(x)
        if t >= 0:
            if y >= 0:
                ans = 2 * abs(y) + 1
            else:
                ans = 2 * abs(y) - 1
        else:
            ans = 2 * abs(x)
        print(ans)
    elif r == 3:
        t = None
        ans = None
        if x >= 0:
            t = abs(x) - abs(y)
        else:
            t = abs(x + 1) - abs(y)
        if t >= 0:
            if x >= 0:
                ans = 2 * abs(x) + 1
            else:
                ans = 2 * abs(x) - 1
        else:
            ans = 2 * abs(y)
        print(ans)
    else:
        ans = 2 * max(abs(x), abs(y))
        if x == y and x != 0:
            ans += 1
        print(ans)
