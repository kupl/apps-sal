def triangular_range(start, stop):
    n = t = 1
    result = {}
    while t <= stop:
        if t >= start:
            result[n] = t
        n += 1
        t = n * (n + 1) // 2
    return result
