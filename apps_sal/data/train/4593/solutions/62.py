def merge_arrays(arr1, arr2):
    ar = arr1 + arr2
    arr = []
    for c in ar:
        if c not in arr:
            arr.append(c)
    arr.sort()  
    return arr
