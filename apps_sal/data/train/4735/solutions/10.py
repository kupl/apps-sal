def keep_order(ary, val):
    ary.append(val)
    return sorted(ary).index(val)
