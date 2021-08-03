from collections import Counter


def revertToDct(lst): return Counter(dict(x[::-1] for x in lst))


def update_inventory(*stocks):
    old, new = map(revertToDct, stocks)
    return [it[::-1] for it in sorted((old + new).items())]
