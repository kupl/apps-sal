def duplicates(array):
    return [n for (i, n) in enumerate(array) if array[:i].count(n) == 1]
