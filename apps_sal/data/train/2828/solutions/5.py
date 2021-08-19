import math


def power_law(x1y1, x2y2, x3):
    if x1y1[0] == x2y2[0]:
        return x2y2[1]  # conner case
    x_asc_rate, y_dsec_rate = x2y2[0] / x1y1[0], x1y1[1] / x2y2[1]
    return round(x2y2[1] / (y_dsec_rate**(math.log(x3 / x2y2[0]) / math.log(x_asc_rate))))
