from functools import reduce


def any_arrows(arrows):
    if arrows:
        return reduce(lambda a, b: a or b, [not a.get('damaged', False) for a in arrows])
    else:
        return False
