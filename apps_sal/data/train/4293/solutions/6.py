def calculate_1RM(w, r):
    if r in (0, 1):
        return (0, w)[r]
    epley = w * (1 + r / 30)
    mcg = 100 * w / (101.3 - 2.67123 * r)
    lomb = w * r ** .1
    return round(max((epley, mcg, lomb)))

