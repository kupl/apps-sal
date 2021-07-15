def flatten(*args):
    return [x for a in args for x in (flatten(*a) if isinstance(a, list) else [a])]
