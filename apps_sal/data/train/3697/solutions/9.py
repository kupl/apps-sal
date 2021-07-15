def list_depth(l):
    return 0 if not isinstance(l, list) else 1 + max(list_depth(x) for x in l) if l else 1

