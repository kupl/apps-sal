from itertools import groupby
def solution(args):
    d=''
    fun = lambda x: x[1] - x[0]
    for k, g in groupby(enumerate(args), fun):
        c=[b for a,b in g]
        if len(c)==1:
            d=d+'%d,'%c[0]
        elif len(c)==2:
            d=d+'%d,%d,'%(c[0],c[-1])
        else:
            d=d+'%d-%d,'%(c[0],c[-1])
    return (d[:-1])
