def merge_arrays(arr1, arr2):
    a = arr1 + arr2
    a.sort()
    mylist = list(dict.fromkeys(a))
    return mylist
