from math import floor


def repos(x, y):
    x = int(floor(x)) + int(round(x))
    y = int(floor(y)) + int(round(y))
    return (x, y)


T = int(input())
for _ in range(T):
    (Ax, Ay, Bx, By, Cx, Cy) = list(map(int, input().split()))
    x = (Ax + Bx + Cx) / 3
    y = (Ay + By + Cy) / 3
    (x, y) = repos(x, y)
    if x == y:
        if x == 0:
            print(0)
        elif x == 1:
            print(1)
        else:
            ans = abs(x) + 1
            print(ans)
    else:
        ans = max(abs(x), abs(y))
        print(ans)
