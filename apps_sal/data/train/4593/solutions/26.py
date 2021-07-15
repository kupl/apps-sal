def merge_arrays(arr1, arr2):
    final_list = []
    for y in arr1:
        if y not in final_list:
            final_list.append(y)
    for x in arr2:
        if x not in final_list:
            final_list.append(x)
    return sorted(final_list)
