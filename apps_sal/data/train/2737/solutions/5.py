from itertools import chain


def flatten(list_):
    return [list_] if isinstance(list_[0], int) else chain(*(flatten(l) for l in list_))


def near_flatten(nested):
    return sorted(chain(*(flatten(list_) for list_ in nested)))
