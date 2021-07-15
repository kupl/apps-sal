from itertools import groupby

def repeat_adjacent(string):
    return(sum(1 for k,g in groupby((sum(1 for _ in g) for _,g in groupby(string)),key=lambda l:l>1) if k==True and next(g) and next(g,None)))
