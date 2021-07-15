import itertools

def number(lines):
    counter=itertools.count(1)
    return [str( next(counter) ) + ": " + x for x in lines]
