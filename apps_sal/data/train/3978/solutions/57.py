def check_for_factor(base, factor):
    if base % factor != 0:
        return False
    elif base % factor == 0:
        return True
