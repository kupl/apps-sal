def merge_arrays(first, second):
    a = list(dict.fromkeys(first + second).keys())
    a.sort()
    return a
