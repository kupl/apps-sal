import sys
input = sys.stdin.readline

def solve(ax,ay,bx,by,cx,cy):
    x = ax+bx+cx
    y = ay+by+cy
    x -= x//3+1
    y -= y//3+1
    if x==y:
        return x if 0 <= x <= 1 else abs(x)+1
    else:
        return max(abs(x), abs(y))

T = int(input())
for _ in range(T):
    ax,ay,bx,by,cx,cy = map(int,input().split())
    print(solve(ax,ay,bx,by,cx,cy))
