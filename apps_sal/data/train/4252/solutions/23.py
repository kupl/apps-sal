def merge_arrays(first, second):
    first.extend(second)
    x = list(dict.fromkeys(first))
    x.sort()
    return x
