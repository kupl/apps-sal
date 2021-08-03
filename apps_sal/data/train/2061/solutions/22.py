def solve(x, y, xd, yd):

    if x + y > 0:
        if x - y > 0:
            return 2 * x + (xd == 1)
        elif x - y < 0:
            return 2 * y + (yd == 1)
        else:
            return 1 + 2 * x + (xd == 1 and yd == 1)
    elif x + y < 0:
        if x - y > 0:
            return -y * 2 - 1 + (yd == 2)
        elif x - y < 0:
            return -x * 2 - 1 + (xd == 2)
        else:
            return -2 * x + (xd == 2 and yd == 2)
    else:
        if x - y > 0:
            return 2 * x + (xd == 1)
        elif x - y < 0:
            return -2 * x + (yd == 1)
        else:
            if xd == 2 and yd == 2:
                return 0
            else:
                return 1


def main():

    t = int(input())
    ans_list = []

    for i in range(t):
        ax, ay, bx, by, cx, cy = list(map(int, input().split()))
        x, y = (min(ax, bx, cx), min(ay, by, cy))
        xd = (ax == x) + (bx == x) + (cx == x)
        yd = (ay == y) + (by == y) + (cy == y)
        ans_list.append(solve(x, y, xd, yd))

    for i in range(t):
        print((ans_list[i]))


main()
