def merge_arrays(arr1, arr2):
    mylist = sorted(arr1 + arr2)
    mylist = list(dict.fromkeys(mylist))
    return mylist
