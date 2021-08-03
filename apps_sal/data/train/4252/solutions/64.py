def merge_arrays(first, second):
    hashing = set()
    for i in first:
        hashing.add(i)
    for j in second:
        hashing.add(j)
    return sorted(list(hashing))
