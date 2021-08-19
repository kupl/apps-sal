def geometric_sequence_elements(a, r, n):
    l = []
    for _ in range(n):
        l.append(str(a))
        a *= r
    return ', '.join(l)
