import math
def past(h, m, s):
    return math.ceil((h * 3.6e+6) + (m * 60000) + (s * 1000))
