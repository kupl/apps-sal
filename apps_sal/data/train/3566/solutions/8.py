from collections import Counter

def find_missing(*args):
    c1,c2 = map(Counter, args)
    return (c1-c2).popitem()[0]
