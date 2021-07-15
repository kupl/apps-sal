def flatten(lst):
    return sum((([x], x)[isinstance(x, list)] for x in lst), [])
