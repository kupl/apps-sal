T = int(input())
for _ in range(T):
    ax,ay,bx,by,cx,cy = map(int,input().split())
    xdis = (ax+bx+cx)-1
    ydis = (ay+by+cy)-1
    if xdis % 3 == 0:
        xneed = abs(xdis)*2//3
    if xdis % 3 == 1:
        xneed = (abs(xdis)*2+1)//3
    if xdis % 3 == 2:
        xneed = (abs(xdis)*2+2)//3
    if ydis % 3 == 0:
        yneed = abs(ydis)*2//3
    if ydis % 3 == 1:
        yneed = (abs(ydis)*2+1)//3
    if ydis % 3 == 2:
        yneed = (abs(ydis)*2+2)//3
    if xdis*ydis > 1 and xneed == yneed:
        print(xneed+1)
    else:
        print(max(xneed,yneed))
