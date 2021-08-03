def merge_arrays(first, second):
    test = list(set(first + second))
    test.sort()
    return test
