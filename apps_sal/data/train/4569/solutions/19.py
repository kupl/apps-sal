from itertools import dropwhile, islice


def next_item(xs, item, nth_successor=1):
    return next(islice(dropwhile(lambda x: x != item, xs), nth_successor, nth_successor + 1), None)
