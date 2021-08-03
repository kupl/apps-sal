from itertools import chain


def flatten(lst):
    try:
        return list(chain.from_iterable(lst))
    except:
        return lst
