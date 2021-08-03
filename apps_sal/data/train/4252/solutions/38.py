def merge_arrays(first, second):
    for i in second:
        if i not in first:
            first.append(i)
    return sorted(list(set(sorted(first))))
