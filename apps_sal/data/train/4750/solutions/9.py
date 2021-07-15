def flatten(a):
    return [x for b in a for x in (b if type(b) is list else [b] ) ]
