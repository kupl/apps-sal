def merge_arrays(arr1, arr2):
    my_List = arr1 + arr2
    a = list(set(my_List))
    return sorted(a)
