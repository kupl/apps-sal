def sum_to_infinity(sequence):
    a = sequence[0]
    r = sequence[1] / a
    return round(a / (1 - r), 3) if -1 < r < 1 else "No Solutions"
