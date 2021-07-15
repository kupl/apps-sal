def flatten(*args):
    
    def _flat(lst):
        for x in lst:
            if isinstance(x,list): yield from _flat(x)
            else:                  yield x
    
    return list(_flat(args))
