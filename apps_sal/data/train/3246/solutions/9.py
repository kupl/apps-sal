from collections import *
def majority(arr):
    for k, v in list(Counter(arr).items()):
        if len(Counter(arr)) == 1: return k
        else:
            if  v > max([j for i, j in list(Counter(arr).items()) if i != k]):
                return k 

