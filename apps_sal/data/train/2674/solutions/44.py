def two_sort(array):
    return "***".join((sorted([x for x in array if x[0].isupper()]) + sorted([x for x in array if x[0].islower()]))[0])
