def sort_by_height(a):
    s = iter(sorted((x for x in a if x != -1)))
    return [x if x == -1 else next(s) for x in a]
