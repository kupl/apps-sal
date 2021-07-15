from itertools import takewhile
def keep_order(ary, val):
    return len(list(takewhile(lambda v: v < val, ary)))

