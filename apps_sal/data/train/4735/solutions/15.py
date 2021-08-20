def keep_order(ary, val):
    return next((i for (i, (v1, v2)) in enumerate(zip(ary, ary[1:]), 1) if v1 <= val <= v2), len(ary)) if ary and val > ary[0] else 0
