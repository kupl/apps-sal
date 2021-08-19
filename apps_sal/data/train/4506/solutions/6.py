def geometric_sequence_elements(a, r, n):
    return ', '.join((str(a * r ** e) for e in range(n)))
