def merge_arrays(arr1, arr2):
    res = []
    (i, k) = (0, 0)
    while i < len(arr1) or k < len(arr2):
        left = arr1[i] if i < len(arr1) else float('inf')
        right = arr2[k] if k < len(arr2) else float('inf')
        if left <= right:
            res.append(left) if not res or res[-1] != left else None
            i += 1
        else:
            res.append(right) if not res or res[-1] != right else None
            k += 1
    return res
