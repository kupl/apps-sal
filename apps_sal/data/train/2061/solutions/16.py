import sys
input = sys.stdin.readline
t = int(input())
cases = [tuple(map(int, input().split())) for _ in range(t)]
ans = []
for (ax, ay, bx, by, cx, cy) in cases:
    abcx = ax + bx + cx
    abcy = ay + by + cy
    (xd, xm) = divmod(abcx, 3)
    (yd, ym) = divmod(abcy, 3)
    x = xd * 2 + xm - 1
    y = yd * 2 + ym - 1
    a = max(abs(x), abs(y))
    if x == y and (x >= 2 or x <= -1):
        a += 1
    ans.append(a)
print(*ans, sep='\n')
