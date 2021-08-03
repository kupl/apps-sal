def arithmetic_sequence_elements(a, r, n):
    rng = list(range(a, a + (r * n), r)) if r != 0 else [a] * n
    return ', '.join(map(str, rng))
