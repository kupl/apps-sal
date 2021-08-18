import sys
input = sys.stdin.readline

r, c, n = map(int, input().split())
L = []


def trans(x, y):
    z = None
    if x == 0:
        z = y
    if y == c:
        z = c + x
    if x == r:
        z = c + r + c - y
    if y == 0:
        z = 2 * r + 2 * c - x
    return z


for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    z1 = trans(x1, y1)
    z2 = trans(x2, y2)
    if z1 is not None and z2 is not None:
        if z1 > z2:
            z1, z2 = z2, z1
        L.append((z1, z2))
        L.append((z2, z1))
L.sort()
cnt = 0
D = dict()
for z1, z2 in L:
    if z1 < z2:
        cnt += 1
        D[z1] = cnt
    else:
        if D[z2] != cnt:
            print("NO")
            return
        cnt -= 1
print("YES")
