def group(lst):
    return [[n] * lst.count(n) for n in sorted(set(lst), key=lst.index)]
