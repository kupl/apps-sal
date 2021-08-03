import itertools


def next_item(xs, item):
    if type(xs) == list or type(xs) == tuple or type(xs) == str:
        try:
            return xs[xs.index(item) + 1]
        except:
            return None
    for i in xs:
        if item == i:
            return next(xs)
