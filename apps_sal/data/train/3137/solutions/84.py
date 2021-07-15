import math

def round_it(n):
    whole, fraction = str(n).split('.')
    if len(whole) < len(fraction):
        final_n = math.ceil(n)
    elif len(whole) > len(fraction):
        final_n = math.floor(n)
    else:
        final_n = round(n)

    return final_n
