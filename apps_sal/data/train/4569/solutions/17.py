from itertools import dropwhile, islice


def next_item(xs, item):
    return next(islice(dropwhile(lambda x: x != item, xs), 1, 2), None)


