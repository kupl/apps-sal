def merge_arrays(arr1, arr2):
    a = arr1 + arr2
    # print(a)
    a.sort()
    mylist = list(dict.fromkeys(a))
    return mylist
