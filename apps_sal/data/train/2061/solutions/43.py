def solv(x,y):
    if x > 0:
        x = x-(x//3) -1
    else:
        x = x+(2-x)//3 -1
    if y > 0:
        y = y-(y//3) -1
    else:
        y = y+(2-y)//3 -1    

    if (x==0 and y==0): return 0
    if (x==1 and y==1): return 1
    return max({x,-x,y,-y}) + (x==y)
 
T = int(input())
for i in range(T):
    x,y = 0,0
    ax,ay,bx,by,cx,cy = list(map(int, input().split()))
    x = ax+bx+cx
    y = ay+by+cy
    print((solv(x,y)))

