def search(a, s):
    s = s.lower()
    return [x for x in a if s in x.lower()]
