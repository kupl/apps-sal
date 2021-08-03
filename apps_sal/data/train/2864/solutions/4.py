def merge_arrays(a, b):
    list = []
    for i in a + b:
        if (a.count(i) == b.count(i) or b.count(i) == 0 or a.count(i) == 0) and i not in list:
            list.append(i)
    return sorted(list)
