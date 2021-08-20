def side_len(x, y):
    return [i for i in range(y - x + 1, x + y) if abs(i ** 2 - y ** 2) != x ** 2]
