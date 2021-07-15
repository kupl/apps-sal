# URL : https://atcoder.jp/contests/arc109/tasks/arc109_d
T = int(input())
for _ in range(T):
    ax, ay, bx, by, cx, cy = list(map(int, input().split()))
    x = ax + bx + cx
    y = ay + by + cy
    if x == y:
        if x == 1:
            print((0))
        elif x == 2:
            print((1))
        elif x > 0:
            if x % 3 == 2:
                print(((x + 1) // 3 * 2))
            else:
                print(((x - 1) // 3 * 2 + 1))
        else:
            x = -x
            if x % 3 == 2:
                print(((x + 1) // 3 * 2 + 1))
            else:
                print(((x + 2) // 3 * 2))
    else:
        res = 0
        for d in (x, y):
            if d % 3 == 2:
                if d > 0:
                    res = max(res, (d - 2) // 3 * 2 + 1)
                else:
                    res = max(res, (-d - 1) // 3 * 2 + 1)
            else:
                if d > 0:
                    res = max(res, (d - 1) // 3 * 2)
                else:
                    res = max(res, (-d + 1) // 3 * 2)
        print(res)

