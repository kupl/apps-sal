def sum_to_infinity(arr):
    (a, b) = arr[:2]
    c = b / a
    return round(a / (1 - c), 3) if -1 < c < 1 else 'No Solutions'
