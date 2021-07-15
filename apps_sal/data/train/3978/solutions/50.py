def check_for_factor(base, factor):
    if base and factor < 0:
        return None
    else:
        a = base % factor
        if a == 0:
            return True
        else:
            return False

