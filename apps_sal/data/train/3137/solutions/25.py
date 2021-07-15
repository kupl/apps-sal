import math
def round_it(n):
    position = str(n).index(".")
    length=len(str(n))-1
    if position < length/2:
        return math.ceil(n)
    elif position > length/2:
        return math.floor(n)
    else: return round(n)
