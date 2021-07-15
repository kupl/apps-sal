from functools import reduce
from operator import xor

def permute_a_palindrome(input_): 
    return len(reduce(xor, [set(c) for c in input_], set())) <= 1
