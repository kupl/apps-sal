from itertools import zip_longest

def normalize(lst, growing=0):
    
    def seeker(lst, d=1):
        yield len(lst), d
        for elt in lst:
            if isinstance(elt,list):
                yield from seeker(elt, d+1)
    
    def grower(lst, d=1):
        return [ grower(o if isinstance(o,list) else [o]*size, d+1)
                    if d != depth else o
                 for o,_ in zip_longest(lst,range(size), fillvalue=growing) ]
                 
    size,depth = map(max, zip(*seeker(lst)))
    return grower(lst)
