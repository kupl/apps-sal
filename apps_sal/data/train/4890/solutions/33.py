from numpy import prod

def find_difference(a, b):
    x , y = prod(a) , prod(b)
    if x > y:
        return x - y
    else:
        return y - x
