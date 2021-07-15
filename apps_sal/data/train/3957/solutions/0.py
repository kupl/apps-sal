from itertools import groupby

def uniq_c(seq): 
    return [ (k,sum(1 for _ in g)) for k,g in groupby(seq)]
