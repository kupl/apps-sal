def animals(x, y):
    b = 0.5 * (y - 2 * x)
    X = (x - b, b)
    return X if all((i // 1 == i and i >= 0 for i in X)) else 'No solutions'
