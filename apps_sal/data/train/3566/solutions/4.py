def find_missing(arr1, arr2):
    for x in set(arr1):
        if arr1.count(x) != arr2.count(x): return x

