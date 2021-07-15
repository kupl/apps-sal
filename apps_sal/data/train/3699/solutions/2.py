def ranks(a):
    return [sorted(a, reverse = True).index(m) + 1 for m in a]
