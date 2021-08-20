def sum_to_infinity(sequence):
    if sequence[1] / sequence[0] < 1 and sequence[1] / sequence[0] > -1:
        return float(str(round(sequence[0] / (1 - sequence[1] / sequence[0]), 3)))
    return 'No Solutions'
