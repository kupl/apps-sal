def is_tune(Q):
    return bool(Q) and any((all(((B - V) % 12 in (0, 2, 4, 5, 7, 9, 11) for B in Q)) for V in range(12)))
