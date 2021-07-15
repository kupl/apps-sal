def list_depth(l):
    try:
        return isinstance(l, list) and max(map(list_depth, l)) + 1
    except:
        return 1
