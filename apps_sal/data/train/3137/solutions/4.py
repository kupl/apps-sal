import math

def round_it(n):
    s = str(n)
    afterDecimal = len(s) - s.index('.') - 1 
    beforeDecimal = len(s) - afterDecimal - 1
    if afterDecimal > beforeDecimal:
        return math.ceil(n)
    elif afterDecimal < beforeDecimal:
        return math.floor(n)
    else:
        return round(n)
