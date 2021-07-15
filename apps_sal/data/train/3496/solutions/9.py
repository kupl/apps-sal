from math import pi

def sort_by_area(seq): 
    return sorted(seq, key = lambda arg: arg[0]*arg[1] if isinstance(arg, tuple) else pi*arg**2)
