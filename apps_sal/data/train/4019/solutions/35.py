def max_multiple(d, b):
    for i in range(b, d, -1):
        if i % d == 0 and i <= b:
            return i
