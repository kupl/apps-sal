from operator import __and__
from functools import reduce


def any_arrows(arrows):
    return not reduce(__and__, [x.get('damaged', False) for x in arrows], True)
