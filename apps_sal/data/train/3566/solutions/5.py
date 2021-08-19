def find_missing(arr1, arr2):
    return next((a for a in set(arr1) if arr1.count(a) != arr2.count(a)))
