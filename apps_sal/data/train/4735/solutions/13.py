def keep_order(ary, val):
    if not ary:
        return 0
    if max(ary) < val:
        return len(ary)
    for i, num in enumerate(ary):
        if num >= val:
            return i
