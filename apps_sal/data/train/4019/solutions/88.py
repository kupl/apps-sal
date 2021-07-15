def max_multiple(d, b):
    i = 1
    start = d
    while d <= b:
        d /= i
        i += 1
        d *= i
    return d-start
