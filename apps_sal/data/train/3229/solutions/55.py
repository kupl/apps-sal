def am_i_wilson(P):
    # https://en.wikipedia.org/wiki/Wilson_prime
    if P == 5 or P == 13 or P == 563:
        return True
    else:
        return False
