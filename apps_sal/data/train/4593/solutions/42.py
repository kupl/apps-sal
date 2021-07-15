def merge_arrays(arr1, arr2):
    final = []
    for el1 in arr1:
        if not el1 in final:
            final.append(el1)
    for el2 in arr2:
        if not el2 in final:
            final.append(el2)
    return sorted(final)
