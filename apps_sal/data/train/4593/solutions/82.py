def merge_arrays(arr1, arr2):
    arr1.extend(arr2)
    arr1.sort()
    result = []
    for i in arr1:
        if i not in result:
            result.append(i)
    return result
