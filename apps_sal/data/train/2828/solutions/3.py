def power_law(a1, a2, x3):
    import math
    x1 = a1[0]
    y1 = a1[1]
    x2 = a2[0]
    y2 = a2[1]
    if x1 == x2:
        return y2
    else:
        return round(y1 * (y2 / y1)**(math.log10(x3 / x1) / math.log10(x2 / x1)))
