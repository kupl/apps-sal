from itertools import groupby

def find(s):
    L = [k*len(list(v)) for k,v in groupby(s)]
    return max((x + y for x,y in zip(L, L[1:])), key=len, default="")
