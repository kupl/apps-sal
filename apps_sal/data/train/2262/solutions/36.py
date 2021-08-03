R, C, n = list(map(int, input().split()))
pair = [list(map(int, input().split())) for _ in range(n)]
u = []
r = []
d = []
l = []
for i in range(n):
    x1, y1, x2, y2 = pair[i]
    if 0 < x1 < R and 0 < y1 < C:
        continue
    if 0 < x2 < R and 0 < y2 < C:
        continue
    if x1 == 0:
        u.append([y1, i])
    if x1 == R:
        d.append([y1, i])
    if y1 == 0:
        if x1 != 0 and x1 != R:
            l.append([x1, i])
    if y1 == C:
        if x1 != 0 and x1 != R:
            r.append([x1, i])
    if x2 == 0:
        u.append([y2, i])
    if x2 == R:
        d.append([y2, i])
    if y2 == 0:
        if x2 != 0 and x2 != R:
            l.append([x2, i])
    if y2 == C:
        if x2 != 0 and x2 != R:
            r.append([x2, i])
u.sort()
r.sort()
d.sort(reverse=True)
l.sort(reverse=True)
urdl = u + r + d + l
stack = []
for i in range(len(urdl)):
    if len(stack) == 0:
        stack.append(urdl[i][1])
    elif stack[-1] == urdl[i][1]:
        stack.pop()
    else:
        stack.append(urdl[i][1])
print("YES" if len(stack) == 0 else "NO")
