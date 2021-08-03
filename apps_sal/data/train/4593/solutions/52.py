def merge_arrays(arr1, arr2):
    lst = list()
    for i in arr2:
        if i not in lst:
            lst.append(i)
    for i in arr1:
        if i not in lst:
            lst.append(i)
    return sorted(lst)
