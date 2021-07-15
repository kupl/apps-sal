def check_for_factor(base, factor):
    if base < 0 or factor < 0:
        return False
    elif base % factor != 0:
        return False
    else:
        return True
