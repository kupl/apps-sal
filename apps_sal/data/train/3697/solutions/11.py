def list_depth(l, f=1):
    return max((f if not isinstance(x, list) else list_depth(x, f + 1) for x in l)) if l else f
