from math import floor
def remainder(dividend, divisor): return "NaN" if divisor == 0 else dividend - floor(dividend / divisor) * divisor
