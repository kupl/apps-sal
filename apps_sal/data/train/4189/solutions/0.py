def highest_value(a, b):
    return max(a, b, key=lambda s: sum(map(ord, s)))
