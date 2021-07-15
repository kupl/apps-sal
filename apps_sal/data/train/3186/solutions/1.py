def similarity(*args):
    a,b = map(set, args)
    return len(a&b) / len(a|b)
