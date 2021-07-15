from operator import mul
def is_orthogonal(u, v): 
    return not sum(map(mul, u, v))
