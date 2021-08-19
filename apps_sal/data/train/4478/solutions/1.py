def sum_to_infinity(sequence):
    sequence = [float(x) for x in sequence]
    (a, r) = (sequence[0], sequence[1] / sequence[0])
    if -1 < r < 1:
        return round(a / (1 - r), 3)
    return 'No Solutions'
