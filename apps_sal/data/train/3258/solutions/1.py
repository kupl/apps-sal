from itertools import groupby
import re

class OutOfFrets(Exception): pass


def convert(k,grp,amount):
    
    def convertOrRaise(m):
        v = int(m.group()) + amount
        if not (0 <= v < 23): raise OutOfFrets()
        return str(v)
        
    lst = list(map(''.join, list(zip(*grp))))
    if isinstance(k,str): return lst

    col  = [re.sub(r'\d+', convertOrRaise, l.strip('-')) for l in lst]
    maxL = max(list(map(len,col)))
    return [l.ljust(maxL, '-') for l in col]
    
    
def transpose(amount, tab):
    try:               lst = [convert(k,g,amount) for k,g in groupby(list(zip(*tab)), key=lambda t: len(set(t))!=1 or t[0])]
    except OutOfFrets: return "Out of frets!"
    
    return list(map(''.join, list(zip(*lst))))

