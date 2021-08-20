def find_difference(a, b):
    x = y = 1
    for (i, j) in zip(a, b):
        x *= i
        y *= j
    return abs(x - y)
