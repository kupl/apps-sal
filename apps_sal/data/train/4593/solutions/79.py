def merge_arrays(arr1, arr2):
    x = []
    for i in arr1:
        x.append(i)
    for j in arr2:
        x.append(j)
    return sorted(list(set(x)))
