def check_for_factor(base, factor):
    if base % factor == 0 or factor % base == 0:
        return True
    else:
        return False
