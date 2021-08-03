def merge_arrays(first, second):
    unique = []
    for f in first:
        if f not in unique:
            unique.append(f)
    for s in second:
        if s not in unique:
            unique.append(s)
    return sorted(unique)
