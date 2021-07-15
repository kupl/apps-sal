def sum_to_infinity(sequence):
    r = sequence[1] / sequence[0]
    if r <= -1 or r >= 1:
        return 'No Solutions'
    sum = sequence[0] / ( 1 - r )
    return round(sum, 3)
