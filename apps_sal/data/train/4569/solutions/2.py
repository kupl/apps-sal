import itertools
def next_item(xs, item):
    try:
        xs = iter(xs)
        for x in xs:
            if x==item: return next(xs)
    except:
        return None
