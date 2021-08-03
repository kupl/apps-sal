def side_len(x, y):
    return [z for z in range(abs(x - y) + 1, x + y) if z * z not in (abs(x * x - y * y), x * x + y * y)]
