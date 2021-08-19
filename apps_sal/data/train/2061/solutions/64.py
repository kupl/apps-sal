T = int(input())
for _ in range(T):
    ax, ay, bx, by, cx, cy = list(map(int, input().split()))
    ldx = min(ax, bx, cx)
    ldy = min(ay, by, cy)
    isleft = int((ax, bx, cx).count(ldx) == 2)
    if ldx > 0:
        transx = ldx + (1 - isleft)
    elif ldx < 0:
        transx = abs(ldx) + isleft - 1
    else:
        transx = 1 - isleft

    isdown = int((ay, by, cy).count(ldy) == 2)
    if ldy > 0:
        transy = ldy + (1 - isdown)
    elif ldy < 0:
        transy = abs(ldy) + isdown - 1
    else:
        transy = 1 - isdown

    # print(ldx, ldy, transx, transy)
    ans = 0
    if ldx == ldy != 0 and (isdown == isleft):
        ans += 1
    # transy = max( transy, abs(ldx))
    # transx = max(transx , (ldy))
    ans += max(transy + abs(ldy), transx + abs(ldx))
    print(ans)
    # print((ax, bx, cx).count(curx) , (ay, by, cy).count(cury))
