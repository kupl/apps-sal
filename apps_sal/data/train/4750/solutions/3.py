from itertools import chain

def flatten(lst):
    try:
        return list(chain(*lst))
    except TypeError:
        return lst
