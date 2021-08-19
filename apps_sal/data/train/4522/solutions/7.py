def side_len(x, y):
    a = ((x ** 2 + y ** 2) ** 0.5, (y ** 2 - x ** 2) ** 0.5)
    return [i for i in range(y - x + 1, y + x) if i not in a]
