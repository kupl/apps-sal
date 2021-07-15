def check_for_factor(base, factor):
    if factor % base == 0:
        return True
    if base % factor == 0:
        return True
    else:
        return False
