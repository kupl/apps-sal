def side_len(x, y):
    return [a for a in range(y - x + 1, x + y) if a * a + x * x != y * y and x * x + y * y != a * a]
