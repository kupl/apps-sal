def triple_trouble(one, two, three):
    tup = list(zip(one, two, three))
    out = list(sum(tup, ()))
    return ''.join(out)
