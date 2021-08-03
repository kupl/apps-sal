def db_sort(arr):
    ints, strg = [], []
    for i in arr:
        ints.append(i) if type(i) == int else strg.append(i)
    return sorted(ints) + sorted(strg)
