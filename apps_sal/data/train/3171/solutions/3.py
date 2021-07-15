from itertools import *

def crashing_weights(arr):
    arr = list(zip(*arr))
    return [list(accumulate(i,lambda x,y: x+y if x>y else y))[-1] for i in arr]
