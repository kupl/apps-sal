def epley(w, r):
    return w * (1 + r / 30)


def mcGlothin(w, r):
    return 100 * w / (101.3 - 2.67123 * r)


def lombardi(w, r):
    return w * r ** 0.1


def calculate_1RM(w, r):
    return r and (w if r == 1 else round(max(epley(w, r), mcGlothin(w, r), lombardi(w, r))))
