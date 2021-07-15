from functools import reduce
def small_enough(A, l): 
    return reduce(lambda a, b: a and b, map(lambda a:a<=l, A))
