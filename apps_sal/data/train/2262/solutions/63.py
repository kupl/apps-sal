(R, C, N) = list(map(int, input().split()))
points = [list(map(int, input().split())) for i in range(N)]


def circ(x, y):
    if y == 0:
        return x
    elif x == R:
        return y + R
    elif y == C:
        return R + C + R - x
    elif x == 0:
        return R + C + R + C - y
    else:
        return -1


L = []
for i in range(N):
    (x1, y1, x2, y2) = points[i]
    if circ(x1, y1) == -1 or circ(x2, y2) == -1:
        continue
    L.append((circ(x1, y1), i))
    L.append((circ(x2, y2), i))
R = [s[1] for s in sorted(L)]
X = []
for i in R:
    if len(X) == 0:
        X.append(i)
    elif X[-1] == i:
        X.pop()
    else:
        X.append(i)
if len(X) == 0:
    print('YES')
else:
    print('NO')
