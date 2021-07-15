def merge_arrays(first, second):
    print(first, second)
    first.extend(second)
    return sorted(list(set(first)))
