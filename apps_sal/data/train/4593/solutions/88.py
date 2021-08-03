def merge_arrays(arr1, arr2):
    list = sorted(arr1 + arr2)
    New_list = []
    for x in list:
        if x not in New_list:
            New_list.append(x)
    return New_list
