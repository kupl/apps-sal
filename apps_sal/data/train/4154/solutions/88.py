def is_triangle(a, b, c):
    x = [a, b, c]
    x.sort()
    if x[2] >= x[0] + x[1]:
        return False
    else:
        return True

