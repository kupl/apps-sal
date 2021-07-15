def sort_by_height(a):
    it = iter(sorted([x for x in a if x >= 0]))
    return [x if x < 0 else next(it) for x in a]
