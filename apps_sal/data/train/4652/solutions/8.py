from math import ceil,log
def score(n):
    return 2**(ceil(log(n,2)))-1 if n>1 else n
