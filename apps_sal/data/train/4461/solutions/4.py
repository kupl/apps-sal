def boxes_packing(length, width, height):
    incr = lambda s: all(x < y for x, y in zip(s, s[1:]))
    return all(incr(s) for s in zip(*sorted(sorted(b) for b in zip(length, width, height))))
