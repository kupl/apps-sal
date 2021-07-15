def merge_arrays(first, second):
    merge, all = [], first + second
    for n in all:
        if n not in merge:
            merge.append(n)
    return sorted(merge)
