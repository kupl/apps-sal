def sum_to_infinity(sequence):
    a = sequence[0]
    r = sequence[1] / sequence[0]
    if r <= -1 or r >= 1:
        return "No Solutions"
    else:
        return round(a / (1 - r), 3)
