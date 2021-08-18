def merge_arrays(first, second):
    first.extend(second)
    x = list(set(first))
    x.sort()
    return x
