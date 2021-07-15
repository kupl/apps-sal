from operator import sub, mul
from functools import reduce

def string_color(string):
    if len(string) < 2:
        return None
    r = sum(map(ord, list(string))) % 256
    g = reduce(mul, list(map(ord, list(string)))) % 256
    b = abs(reduce(sub, list(map(ord, list(string))))) % 256
    return '{:02X}{:02X}{:02X}'.format(r,g,b) 

