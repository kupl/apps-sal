def _trips(x, y):
    return [(x ** 2 + y ** 2) ** 0.5, (y ** 2 - x ** 2) ** 0.5]


def side_len(x, y):
    return [i for i in range(y - x + 1, x + y) if i not in _trips(x, y)]
