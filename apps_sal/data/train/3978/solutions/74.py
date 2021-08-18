def check_for_factor(base, factor):
    remainder = base % factor
    if remainder == 0:
        return True
    else:
        return False
