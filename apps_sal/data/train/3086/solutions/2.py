from itertools import islice

def unflatten(a):
    it = iter(a)
    return [x if x < 3 else [x] + list(islice(it, 0, x-1)) for x in it]
