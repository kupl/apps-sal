def geometric_sequence_elements(a, r, n):
    res = [a]
    for i in range(n - 1):
        res.append(res[-1] * r)
    return ', '.join(map(str, res))
