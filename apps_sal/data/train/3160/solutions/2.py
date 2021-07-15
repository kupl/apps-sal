from functools import reduce

def multi(lst):
    return reduce(lambda m, n: m * n, lst, 1)
    
def add(lst):
    return sum(lst)
    
def reverse(string):
    return string[::-1]
