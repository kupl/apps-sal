def langtons_ant(n):
    k = (n - 11000) // 104 if n > 11000 else 0
    blacks = set()
    (x, y) = (0, 0)
    (dx, dy) = (0, 1)
    for _ in range(n - k * 104):
        if (x, y) in blacks:
            blacks.remove((x, y))
            (dx, dy) = (dy, -dx)
        else:
            blacks.add((x, y))
            (dx, dy) = (-dy, dx)
        (x, y) = (x + dx, y + dy)
    return len(blacks) + k * 12
