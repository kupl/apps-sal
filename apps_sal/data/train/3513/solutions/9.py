def folding(a, b):
    n = 1
    while a != b:
        n += 1
        a, b = abs(a - b), min(a, b)
    return n
