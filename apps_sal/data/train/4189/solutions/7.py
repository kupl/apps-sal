def highest_value(a, b):
    return [a, b][sum(map(ord, a)) < sum(map(ord, b))]
