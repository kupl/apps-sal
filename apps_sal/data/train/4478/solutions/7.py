def sum_to_infinity(l):
    return 'No Solutions' if abs(l[1]) >= abs(l[0]) else round(l[0] / (1 - l[1] / l[0]), 3)
