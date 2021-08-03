def find_array(arr1, arr2):
    arr2 = set(arr2)
    return [n for i, n in enumerate(arr1) if i in arr2]
