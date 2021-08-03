def keep_order(ary, val):
    for i, _ in enumerate(ary):
        if val <= ary[i]:
            return i
    return len(ary)
