def fence(n, m, k, coords):
    dirs = [(0, -1), (0, 1), (1, 0), (-1, 0)]
    f = 0
    for coord in coords:
        for (dx, dy) in dirs:
            (x, y) = (coord[0] + dx, coord[1] + dy)
            if x >= 0 and x < n and (y >= 0) and (y < m) and ((x, y) in coords):
                pass
            else:
                f += 1
    return f


t = int(input())
for _ in range(t):
    (n, m, k) = map(int, input().split())
    L = []
    for _ in range(k):
        (a, b) = map(int, input().split())
        L.append((a - 1, b - 1))
    coords = set(L)
    print(fence(n, m, k, coords))
