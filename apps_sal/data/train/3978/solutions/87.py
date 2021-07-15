def check_for_factor(base, factor):
    if factor == 0:
        return False
    else:
        return(base % factor == 0)
