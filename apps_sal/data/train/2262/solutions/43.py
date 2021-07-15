R, C, N = list(map(int, input().split()))
pts = []
for i in range(N):
    x1, y1, x2, y2 = list(map(int, input().split()))
    zs = []
    for x, y in [(x1, y1), (x2, y2)]:
        if y == 0:
            zs.append((x, i))
        elif x == R:
            zs.append((R+y, i))
        elif y == C:
            zs.append((2*R+C-x, i))
        elif x == 0:
            zs.append((2*R+2*C-y, i))
    if len(zs) == 2:
        pts += zs

pts.sort()

stack = []
for z, i in pts:
    if not stack:
        stack.append(i)
    else:
        if stack[-1] == i:
            stack.pop()
        else:
            stack.append(i)

if not stack:
    print('YES')
else:
    print('NO')

