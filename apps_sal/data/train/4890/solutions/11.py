from functools import reduce
def find_difference(a, b): return abs(reduce(lambda x, y: x * y, a) - reduce(lambda x, y: x * y, b))
