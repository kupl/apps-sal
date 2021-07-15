def check_for_factor(base, factor):
    print(base, factor)
    if base > factor:
        return base % factor == 0
    else:
        return factor % base == 0
