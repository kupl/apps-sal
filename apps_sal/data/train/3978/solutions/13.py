def check_for_factor(base, factor):
    return factor in [i for i in range(1, base + 1) if base % i == 0]
