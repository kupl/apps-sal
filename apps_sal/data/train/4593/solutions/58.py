def merge_arrays(arr1, arr2):
    for x in arr2:
        arr1.append(x)
    a=set(arr1)
    b=list(a)
    b.sort()
    return b
