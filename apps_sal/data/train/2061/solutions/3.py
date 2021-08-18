T = int(input())


def calc(ax, ay, bx, by, cx, cy):
    GL = min(ax, bx, cx)
    GU = min(ay, by, cy)
    xcnt = {}
    for x in (ax, bx, cx):
        xcnt[x] = xcnt.get(x, 0) + 1
    ycnt = {}
    for y in (ay, by, cy):
        ycnt[y] = ycnt.get(y, 0) + 1

    if GL == 0 and GU == 0:
        if xcnt[0] == 2 and ycnt[0] == 2:
            ret = 0
        else:
            ret = 1
    else:
        ret = int(GL > 0)
        ret += min(abs(GL), abs(GU)) * 2
        if abs(GU) > abs(GL):
            ret += 1
        ret += max(0, abs(abs(GU) - abs(GL)) * 2 - 1)
        if abs(GU) >= abs(GL):
            if GU > 0:
                if ycnt[GU] == 1:
                    ret += 1
            else:
                if ycnt[GU] == 2:
                    ret += 1
        else:
            if GL > 0:
                if xcnt[GL] == 1:
                    ret += 1
            else:
                if xcnt[GL] == 2:
                    ret += 1
    return ret


for _ in range(T):
    ax, ay, bx, by, cx, cy = map(int, input().split())

    ans0 = calc(ax, ay, bx, by, cx, cy)
    ans1 = calc(ay, ax, by, bx, cy, cx)

    ans = min(ans0, ans1)
    print(ans)
