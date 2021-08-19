def db_sort(arr):
    (strings, integers) = ([], [])
    for i in arr:
        integers.append(i) if type(i) is int else strings.append(i)
    return sorted(integers) + sorted(strings)
