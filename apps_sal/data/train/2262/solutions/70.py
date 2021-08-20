(R, C, N) = map(int, input().split())
edge = []


def F(x, y):
    if x == 0:
        return y
    if y == C:
        return C + x
    if x == R:
        return R + C * 2 - y
    if y == 0:
        return 2 * R + 2 * C - x
    return -1


for i in range(1, N + 1):
    (x1, y1, x2, y2) = map(int, input().split())
    d1 = F(x1, y1)
    d2 = F(x2, y2)
    if d1 < 0:
        continue
    if d2 < 0:
        continue
    edge.append((d1, i))
    edge.append((d2, i))
edge.sort()
stack = []
used = [False] * (N + 1)
ans = 'YES'
for (_, x) in edge:
    if not used[x]:
        used[x] = True
        stack.append(x)
    else:
        y = stack.pop()
        if x != y:
            ans = 'NO'
            break
print(ans)
