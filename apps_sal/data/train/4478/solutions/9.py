def sum_to_infinity(seq):
    r = seq[1] / seq[0]
    return round(seq[0] / (1 - r), 3) if -1 < r < 1 else 'No Solutions'
