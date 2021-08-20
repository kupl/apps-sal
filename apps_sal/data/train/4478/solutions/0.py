def sum_to_infinity(sequence):
    return round(sequence[0] / (1 - sequence[1] / sequence[0]), 3) if abs(sequence[1] / sequence[0]) < 1 else 'No Solutions'
