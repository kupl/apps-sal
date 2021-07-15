from itertools import groupby
def reverse(str):
    reversal=""
    for k,g in groupby(str):
        l=list(g)
        if len(l)>1:reversal+=''.join(l).swapcase()
        else:reversal+=k
    return reversal
