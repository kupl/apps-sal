def check_for_factor(base, factor):
    if base >= 0 and factor >= 0:
        if base % factor == 0:
            return True
        else:
            return False
