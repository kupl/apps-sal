def list_depth(l):
    return (1 + max((list_depth(item) for item in l), default=0)) if type(l) == list else 0

