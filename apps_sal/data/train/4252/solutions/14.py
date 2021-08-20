def merge_arrays(arr1, arr2):
    merged = []
    (i, k) = (0, 0)
    while i < len(arr1) and k < len(arr2):
        (left, right) = (arr1[i], arr2[k])
        if left <= right:
            merged.append(left)
            i += 1
        else:
            merged.append(right)
            k += 1
    merged.extend(arr1[i:] if i < len(arr1) else arr2[k:])
    merged = list(dict.fromkeys(merged))
    return merged
