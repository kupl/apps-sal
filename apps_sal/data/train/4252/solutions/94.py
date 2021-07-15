def merge_arrays(first, second):
    for i in first:
        while first.count(i)>1:
            first.remove(i)
    for i in second:
        if not i in first:
            first.append(i)
    first.sort()
    return first
