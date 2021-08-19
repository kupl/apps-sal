def find_next_power(n, p):
    return int(n ** (1.0 / p) + 1) ** p
