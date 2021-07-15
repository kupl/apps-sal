from itertools import chain

def unite_unique(*arrs):
    r = list ()
    
    for item in chain (*arrs):
        if item not in r:
            r.append (item)

    return r

