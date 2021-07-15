def side_len(a, b):
    r = ((a*a + b*b)**0.5, (b*b - a*a)**0.5)
    return [c for c in range(b-a+1, a+b) if c not in r]
