def list_depth(l):
    if l == []:
        return 1
    if isinstance(l, list):
        return 1 + max((list_depth(item) for item in l))
    else:
        return 0
