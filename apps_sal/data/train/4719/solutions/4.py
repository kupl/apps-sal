def sort_array(a):
    e, o = sorted(x for x in a if x % 2 ^ 1), sorted((x for x in a if x % 2), reverse=True)
    return [(o if x % 2 else e).pop() for x in a]
