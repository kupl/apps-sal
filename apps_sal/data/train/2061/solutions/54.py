t = int(input())
buf = []
for _ in range(t):
    ax, ay, bx, by, cx, cy = list(map(int, input().split()))

    mx = min(ax, bx, cx)
    my = min(ay, by, cy)

    dx = (ax == mx) + (bx == mx) + (cx == mx)
    dy = (ay == my) + (by == my) + (cy == my)

    if mx == 0 and my == 0:
        if dx == 2 and dy == 2:
            buf.append(0)
        else:
            buf.append(1)
        continue

    rx, ry = False, False
    if mx < 0:
        mx = -mx
        dx = 3 - dx
        rx = True
    if my < 0:
        my = -my
        dy = 3 - dy
        ry = True

    ans = 2 * max(mx, my)

    if mx == my:
        ans += 1
        if rx or ry:
            ans -= 1
            if (rx == False and dx == 1) or (ry == False and dy == 1):
                ans += 1
            elif rx and ry and dx == 1 and dy == 1:
                ans += 1
        elif dx == 1 and dy == 1:
            ans += 1
    elif mx > my:
        if rx:
            ans -= 1
        if dx == 1:
            ans += 1
    elif mx < my:
        if ry:
            ans -= 1
        if dy == 1:
            ans += 1

    # print(_, mx, my, dx, dy, ans)

    buf.append(ans)

print(('\n'.join(map(str, buf))))

