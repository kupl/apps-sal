def sum_to_infinity(sequence):
    (x, y) = sequence[:2]
    return round(x * x / (x - y), 3) if abs(x) > abs(y) else 'No Solutions'
