def cycle(lst):
    return next(([i, lst.index(n, i+1)-i] for i, n in enumerate(lst) if n in lst[i+1:]), [])

