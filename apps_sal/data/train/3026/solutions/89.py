def min_value(d):
    dd = sorted(list(set(d)))
    smallest = dd[0]
    for i in range(1, len(dd)):
        smallest *= 10
        smallest += dd[i]
    return smallest
