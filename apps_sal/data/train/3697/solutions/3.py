def list_depth(l):
    return max((1+list_depth(x) for x in l if isinstance(x, (list, tuple))), default=1)
