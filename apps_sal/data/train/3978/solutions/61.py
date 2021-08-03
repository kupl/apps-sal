def check_for_factor(base, factor):
    x = base % factor
    if x == 0:
        return True
    else:
        return False
