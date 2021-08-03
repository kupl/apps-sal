def merge_arrays(arr1, arr2):
    for arr in (arr1, arr2):
        if arr[0] > arr[-1]:
            arr.reverse()
    res = []
    i = 0
    k = 0
    while not(i >= len(arr1) and k >= len(arr2)):
        left = arr1[i] if i < len(arr1) else float("inf")
        right = arr2[k] if k < len(arr2) else float("inf")
        res_last = res[-1] if res else None
        if left <= right:
            res_last != left and res.append(left)
            i += 1
        else:
            res_last != right and res.append(right)
            k += 1
    return res
