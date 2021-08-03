def sum_arrays(arr1, arr2):
    if not arr1 and not arr2:
        return []
    if any([not arr1, not arr2]):
        return arr1 if not arr2 else arr2
    a = str(int("".join([str(x) for x in arr1])) + int("".join([str(x) for x in arr2])))
    if a == "0":
        return []
    return [-int(a[1])] + [int(a[k]) for k in range(2, len(a))] if a[0] == "-" else [int(a[k]) for k in range(len(a))]
