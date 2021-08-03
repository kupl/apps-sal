def side_len(x, y):
    return [i for i in range(abs(x - y) + 1, abs(x + y)) if i != (x * x + y * y)**0.5 and i != abs(y * y - x * x)**0.5]
