def check_for_factor(base, factor):
    check = base % factor
    if check > 0:
        return False
    else:
        return True
