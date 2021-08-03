def folding(a, b):
    squares = 1
    while a != b:
        squares += 1
        b, a = sorted((a - b, b))
    return squares
