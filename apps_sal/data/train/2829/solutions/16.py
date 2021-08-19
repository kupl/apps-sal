def array_madness(*args):
    return int.__gt__(*(sum(map(i.__rpow__, arr)) for (i, arr) in enumerate(args, 2)))
