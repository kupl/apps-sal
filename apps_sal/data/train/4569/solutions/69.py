import itertools
def next_item(xs, item):
    next_item = None
    if type(xs) is itertools.count:
        for i in xs:
            if i == item:
                next_item = next(xs)
                break
    else:
        list_xs = list(xs)
        for n, x in enumerate(list_xs):
            if item == list_xs[n] and n < len(list_xs)-1:
                next_item = list_xs[n+1]
                break
    return next_item
