def distinct(seq):
    a = set()
    return [x for x in seq if x not in a and (not a.add(x))]
