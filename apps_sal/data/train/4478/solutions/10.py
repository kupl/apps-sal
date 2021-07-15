def sum_to_infinity(a):
    return round(a[0] / (1 - a[1]/a[0]), 3) if -1 < a[1]/a[0] < 1 else 'No Solutions'

