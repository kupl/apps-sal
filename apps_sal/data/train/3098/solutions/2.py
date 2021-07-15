from itertools import count

def compute_depth(n):
    found = set()
    update = found.update
    return next(i for i,x in enumerate(count(n, n), 1) if update(str(x)) or len(found) == 10)
