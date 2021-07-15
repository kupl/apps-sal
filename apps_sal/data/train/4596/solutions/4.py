import math
import functools
import operator

def perms(element):
    element = str(element)
    permutation_count = math.factorial(len(element))
    eq_bottom = [math.factorial(element.count(char)) for char in set(element)]       
    combination_count = functools.reduce(operator.mul, eq_bottom, 1)
    return permutation_count / combination_count
