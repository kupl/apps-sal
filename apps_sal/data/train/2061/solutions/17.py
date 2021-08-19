def coord1d(a, b, c):
    m = max(a, max(b, c))
    ct = 0
    if a == m:
        ct += 1
    if b == m:
        ct += 1
    if c == m:
        ct += 1
    if ct == 1:
        return m * 2 - 1
    else:
        return m * 2


def coord(ax, ay, bx, by, cx, cy):
    newx = coord1d(ax, bx, cx)
    newy = coord1d(ay, by, cy)
    return (newx, newy)


T = int(input())
for _ in range(T):
    (ax, ay, bx, by, cx, cy) = list(map(int, input().split()))
    (nx, ny) = coord(ax, ay, bx, by, cx, cy)
    ans = 0
    if nx == ny and (not (nx == 1 or nx == 2)):
        ans = abs(nx - 1) + 1
    else:
        ans = max(abs(nx - 1), abs(ny - 1))
    print(ans)
