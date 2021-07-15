import math

def round_it(n):
    left, right = str(n).split('.')
    if len(left) < len(right):
        result = math.ceil(n)
    elif len(left) > len(right):
        result = math.floor(n)
    else:
        result = round(n)
    return result
