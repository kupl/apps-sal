def transform(a):
    m = max(a)
    return [m - element for element in a]


def array_operations(a, k):
    return transform(a) if k % 2 == 1 else transform(transform(a))
