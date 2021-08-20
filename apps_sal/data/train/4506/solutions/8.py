def geometric_sequence_elements(a, r, n):
    seq = []
    for i in range(n):
        seq.append(a * r ** i)
    return ', '.join((str(e) for e in seq))
