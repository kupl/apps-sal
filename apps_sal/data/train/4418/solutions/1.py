def get_function(sequence):
    first, dist = sequence[0], sequence[1] - sequence[0]
    valid = all(x == dist * i + first for i, x in enumerate(sequence))
    def f(x): return dist * x + first
    return f if valid else 'Non-linear sequence'
