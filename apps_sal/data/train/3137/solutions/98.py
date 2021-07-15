import math
def round_it(n):
    nn = str(n)
    lhs, rhs = nn.split('.')
    if len(lhs)>len(rhs):
        return math.floor(n)
    elif len(lhs)<len(rhs):
        return math.ceil(n)
    else:
        return round(n)
