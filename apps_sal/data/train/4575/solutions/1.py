from itertools import filterfalse, chain, count

def smallest_integer(matrix):
    return next(filterfalse(set(chain.from_iterable(matrix)).__contains__, count()))
