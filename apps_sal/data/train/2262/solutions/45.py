r, c, n = list(map(int, input().split()))
l = []
for i in range(n):
    x1, y1, x2, y2 = list(map(int, input().split()))
    if (x1 == 0 or x1 == r or y1 == 0 or y1 == c) and (x2 == 0 or x2 == r or y2 == 0 or y2 == c):
        if x1 == 0:
            l.append((y1, i))
        elif y1 == c:
            l.append((c + x1, i))
        elif x1 == r:
            l.append((c * 2 + r - y1, i))
        else:
            l.append((r * 2 + c * 2 - x1, i))
        if x2 == 0:
            l.append((y2, i))
        elif y2 == c:
            l.append((c + x2, i))
        elif x2 == r:
            l.append((c * 2 + r - y2, i))
        else:
            l.append((r * 2 + c * 2 - x2, i))
l.sort()
s = []
d = [False] * n
for x, i in l:
    if d[i]:
        if s[-1] != i:
            print('NO')
            return
        s.pop()
    else:
        s.append(i)
        d[i] = True
print('YES')

