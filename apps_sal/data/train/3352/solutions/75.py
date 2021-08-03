def find_longest(a):
    return sorted([x for x in a], key=lambda x: -len(str(x)))[0]
