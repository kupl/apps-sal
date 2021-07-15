from math import log10

def find_longest(arr):
    return max(arr,key=lambda n:int(log10(n)))
