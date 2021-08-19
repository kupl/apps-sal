def check_for_factor(base, factor):
    i = base % factor
    if i == 0:
        return True
    else:
        return False
