def check_for_factor(base, factor):
    a = base % factor
    if a == 0:
        c = True
    else:
        c = False
    return c
