def is_triangle(a, b, c):
    lengths = [a, b, c]
    x = sorted(lengths)
    print((x, x[0] + x[1]))
    if x[0] + x[1] > x[2]:
        return True
    else:
        return False
