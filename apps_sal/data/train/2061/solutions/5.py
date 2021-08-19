import sys
from collections import deque

T = int(input())
# 0 L
# 1 |-
# 2 -|
# 3 _|


def ku_state(p1, p2, p3):
    xb = min([p[0] for p in [p1, p2, p3]])
    yb = min([p[1] for p in [p1, p2, p3]])
    s = set([(p[0] - xb, p[1] - yb) for p in [p1, p2, p3]])
    if len(s) != 3 or max([x[0] for x in s]) != 1 or max([x[1] for x in s]) != 1:
        return None
    if (1, 1) not in s:
        return 0
    elif (1, 0) not in s:
        return 1
    elif (0, 0) not in s:
        return 2
    elif (0, 1) not in s:
        return 3
    else:
        return None


for _ in range(T):
    ax, ay, bx, by, cx, cy = list(map(int, input().split()))
    ps = [(ax, ay), (bx, by), (cx, cy)]
    ku = (ku_state(*ps))
    xb = min(ax, bx, cx)
    yb = min(ay, by, cy)
    xd = int(abs(xb + 0.5))
    yd = int(abs(yb + 0.5))
    if xb == 0 and yb == 0:
        print((int(ku != 0)))
        continue
    if ku == 0:
        ans = max(abs(xb), abs(yb)) * 2
        if xb == yb:
            ans += 1
    elif ku == 1:
        ans = max(abs(xb) * 2, 2 * yd + 1)
        ans = max(1, ans)
    elif ku == 2:
        if xb == 0 and yb == 0:
            ans = 1
        else:
            ans = max(xd, yd) * 2 + 1
            if xb == yb:
                ans += 1
    elif ku == 3:
        ans = max(abs(yb) * 2, 2 * xd + 1)
        ans = max(1, ans)
    print(ans)
