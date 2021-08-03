def merge_arrays(arr1, arr2):
    b = []
    a = arr1 + arr2
    [b.append(i) for i in a if i not in b]
    b.sort()
    return b
