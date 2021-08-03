def keep_order(ary, val):
    return next((ary.index(x) for x in ary if x >= val), len(ary))
