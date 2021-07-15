def merge_arrays(arr1, arr2):
    #merge then sort
    arr = arr1+arr2
    empty = []
    for i in arr:
        if i not in empty:
            empty.append(i)
    return sorted(empty)

