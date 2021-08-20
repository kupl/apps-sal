def chess_triangle(n, m):
    return (lambda x, y: 0 if x < 2 else max(0, 16 * y - 40) if x == 2 else 240 + 64 * y * (x - 2) - 128 * x)(*sorted([n, m]))
