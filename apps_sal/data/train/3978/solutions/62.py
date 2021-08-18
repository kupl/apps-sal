def check_for_factor(base, factor):
    base = int(base)
    factor = int(factor)
    if base % factor == 0:
        return True
    else:
        return False
