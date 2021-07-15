import itertools
def nth(iterable, n, default=None):
    return next(itertools.islice(iterable, n, None), default)

def next_item (xs,item):
     a=itertools.dropwhile(lambda x: x!=item,xs)
     return nth(a,1,None)
       

