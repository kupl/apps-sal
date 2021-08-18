def find_deleted_number(arr, mixed_arr):
    ret = 0
    for i in arr:
        if i not in mixed_arr:
            ret = i

    return ret
