from functools import reduce
def logical_calc(array, op): return reduce(lambda a, b: a and b if op == "AND" else a or b if op == "OR" else a != b, array)
