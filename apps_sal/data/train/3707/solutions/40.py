def sorter(textbooks):
    x = sorted(textbooks, key = lambda s: s.casefold())
    return x
