from sys import stdin, stdout
(r, c, n) = map(int, stdin.readline().split())
fx = {}
fy = {}
s = set()
for _ in range(n):
    (x, y) = stdin.readline().split()
    fx[x] = fx.get(x, 0) + 1
    fy[y] = fy.get(y, 0) + 1
    s.add((x, y))
(xl, xn) = ([], max(fx.values()))
for x in fx:
    if fx[x] == xn:
        xl.append(x)
(yl, yn) = ([], max(fy.values()))
for y in fy:
    if fy[y] == yn:
        yl.append(y)
count = xn + yn - 1
broken = False
for x in xl:
    for y in yl:
        if (x, y) not in s:
            broken = True
            break
    if broken:
        break
stdout.write(str(count + broken))
