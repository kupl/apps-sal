def reflections(n, m):
    x = y = 0
    dx = dy = 1
    while 1:
        x += dx
        y += dy
        if x == y == 0 or x == n and y == m:
            return 1
        if 0 in (x, y) and (x == n or y == m):
            return 0
        if x in (0, n):
            dx *= -1
        if y in (0, m):
            dy *= -1
