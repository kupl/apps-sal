def find_next_power(val, pow_):
    import math
    a = val ** (1.0 / pow_)
    b = math.ceil(a)
    return b ** pow_
