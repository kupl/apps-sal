from itertools import accumulate
def add(l):
    return list(accumulate(l)) if isinstance(l, list) and all(isinstance(x, int) for x in l) \
        else 'Invalid input'
