def check_for_factor(base, factor):
    for n in range(1, base):
        if base % (factor * n) == 0:
            return True
        else:
            return False
