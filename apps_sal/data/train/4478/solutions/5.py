def sum_to_infinity(seq):
    if len(seq) < 2:
        return 'No Solutions'
    r = seq[1] / seq[0]
    if r >= 1 or r <= -1:
        return 'No Solutions'
    return 1 if seq[0] == seq[1] else round(seq[0] / (1 - r), 3)
