from collections import Iterable

def unpack(iterable):
    lst = []
    for x in iterable:
        if   isinstance(x,dict):     x = unpack(x.items())
        elif isinstance(x,str):      x = [x]
        elif isinstance(x,Iterable): x = unpack(x)
        else:                        x = [x]
        lst.extend(x)
    return lst
