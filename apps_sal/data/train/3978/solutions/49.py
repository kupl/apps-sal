def check_for_factor(base, factor):
    if base % factor == 0 and base > 0:
        return True
    elif base is None:
        return False
    else:
        return False
