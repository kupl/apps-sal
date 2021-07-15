import math as MATHEMATICA
def odd_count(n):
    return MATHEMATICA.ceil(n/2)-1 if n%2 != 0 else MATHEMATICA.ceil(n/2)
