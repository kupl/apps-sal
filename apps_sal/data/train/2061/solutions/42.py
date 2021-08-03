ansl = []
for q in range(int(input())):
    ax, ay, bx, by, cx, cy = map(int, input().split())
    fs = [(0, 0), (0, 1), (1, 0)]
    fs2 = [(-1, 0), (0, 0), (0, -1)]
    if (ax, ay) in fs and (bx, by) in fs and (cx, cy) in fs:
        ansl.append(0)
        continue
    if (ax, ay) in fs2 and (bx, by) in fs2 and (cx, cy) in fs2:
        ansl.append(2)
        continue
    if (ax, ay) == (0, 0) or (bx, by) == (0, 0) or (cx, cy) == (0, 0):
        ans = 0
        if (ax, ay) not in fs:
            ans += 1
        if (bx, by) not in fs:
            ans += 1
        if (cx, cy) not in fs:
            ans += 1
        ansl.append(ans)
        continue

    if abs(ax) <= abs(ay) and abs(bx) <= abs(by) and abs(cx) <= abs(cy):
        ax, ay = ay, ax
        bx, by = by, bx
        cx, cy = cy, cx
    if abs(ax) >= abs(ay) and abs(bx) >= abs(by) and abs(cx) >= abs(cy):
        miny = min(ay, by, cy)
        ay -= miny
        by -= miny
        cy -= miny
        samex = 0
        if ax == bx:
            samex = ax
            difx = cx
        elif bx == cx:
            samex = bx
            difx = ax
        else:
            samex = cx
            difx = bx
        if difx < samex:
            dist = difx * 2 + 1
        else:
            dist = samex * 2
        dist = max(dist, dist * (-1))
        ansl.append(dist)

    else:
        xp = 0
        yp = 0
        if abs(ax) == abs(ay):
            xp = ax
            yp = ay
        elif abs(bx) == abs(by):
            xp = bx
            yp = by
        elif abs(cx) == abs(cy):
            xp = cx
            yp = cy

        if xp >= 0 and yp >= 0:
            if max(ay, by, cy) == yp:
                if xp == 1:
                    dist = 1
                else:
                    dist = abs(xp) * 2
            else:
                dist = abs(xp) * 2 + 1
        elif xp < 0 and yp < 0:
            if max(ay, by, cy) == yp:
                dist = abs(xp) * 2 + 2
            else:
                dist = abs(xp) * 2 + 1
        elif xp >= 0 and yp < 0:
            if max(ay, by, cy) == yp:
                dist = abs(xp) * 2 + 1
            else:
                dist = abs(xp) * 2
        else:
            if max(ay, by, cy) == yp:
                dist = abs(xp) * 2
            else:
                dist = abs(xp) * 2 + 1
        ansl.append(dist)

for a in ansl:
    print(a)
