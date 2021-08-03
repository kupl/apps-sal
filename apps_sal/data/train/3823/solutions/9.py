def deep_count(a):
    if a == []:
        return 0
    if isinstance(a[0], list):
        return 1 + deep_count(a[0]) + deep_count(a[1:])
    return 1 + deep_count(a[1:])
