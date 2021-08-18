import sys
input = sys.stdin.readline

R, C, N = map(int, input().split())
right = []
top = []
left = []
bottom = []
for i in range(N):
    x1, y1, x2, y2 = map(int, input().split())
    if (x1 in (0, R) or y1 in (0, C)) and (x2 in (0, R) or y2 in (0, C)):
        if x1 == 0:
            top.append((y1, i))
        elif x1 == R:
            bottom.append((y1, i))
        elif y1 == 0:
            left.append((x1, i))
        elif y1 == C:
            right.append((x1, i))

        if x2 == 0:
            top.append((y2, i))
        elif x2 == R:
            bottom.append((y2, i))
        elif y2 == 0:
            left.append((x2, i))
        elif y2 == C:
            right.append((x2, i))
left.sort(key=lambda p: p[0])
bottom.sort(key=lambda p: p[0])
right.sort(key=lambda p: -p[0])
top.sort(key=lambda p: -p[0])
points = left + bottom + right + top
stack = []
for x, i in points:
    if not stack or stack[-1] != i:
        stack.append(i)
    else:
        stack.pop()
print('NO' if stack else 'YES')
