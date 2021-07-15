def check_for_factor(base, factor):
    case = base % factor
    if case == 0:
        return True
    else:
        return False
