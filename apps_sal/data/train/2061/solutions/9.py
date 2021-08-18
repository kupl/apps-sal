def get_center(ps):
    xs, ys = list(zip(*ps))
    xs, ys = list(xs), list(ys)
    xs.sort()
    ys.sort()
    return xs[1], ys[1]


def get_shape(ps):
    """
    0: 
    """
    xs, ys = list(zip(*ps))
    xs, ys = list(xs), list(ys)
    xs.sort()
    ys.sort()
    if xs[0] == xs[1] and ys[0] == ys[1]:
        return 0
    elif xs[0] == xs[1] and ys[1] == ys[2]:
        return 1
    elif xs[1] == xs[2] and ys[0] == ys[1]:
        return 2
    else:
        return 3


t = int(input())


for _ in range(t):
    x1, y1, x2, y2, x3, y3 = map(int, input().split())
    ps = [(x1, y1), (x2, y2), (x3, y3)]

    cx, cy = get_center(ps)
    shape = get_shape(ps)

    if cx == 0 and cy == 0:
        if shape == 0:
            print(0)
        elif shape == 1:
            print(1)
        elif shape == 2:
            print(1)
        else:
            print(2)
    elif cx == 1 and cy == 1:
        if shape == 0:
            print(3)
        elif shape == 1:
            print(2)
        elif shape == 2:
            print(2)
        else:
            print(1)
    elif cx == cy:
        if cx > 0:
            if shape == 0:
                print(2 * cx + 1)
            else:
                print(2 * cx)
        else:
            if shape == 3:
                print(2 - 2 * cx)
            else:
                print(1 - 2 * cx)
    else:
        if abs(cx) > abs(cy) and cx > 0:
            if shape == 0 or shape == 1:
                print(cx * 2)
            else:
                print(cx * 2 - 1)
        elif abs(cx) >= abs(cy) and cx < 0:
            if shape == 0 or shape == 1:
                print(-cx * 2)
            else:
                print(-cx * 2 + 1)
        elif abs(cx) < abs(cy) and cy > 0:
            if shape == 0 or shape == 2:
                print(cy * 2)
            else:
                print(cy * 2 - 1)
        else:
            if shape == 0 or shape == 2:
                print(-cy * 2)
            else:
                print(-cy * 2 + 1)
