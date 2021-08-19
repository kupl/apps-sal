def find_array(arr1, arr2):
    return list() if not arr1 or not arr2 else [arr1[i] for i in arr2 if i <= len(arr1)]
