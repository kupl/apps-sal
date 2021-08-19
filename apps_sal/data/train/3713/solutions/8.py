def find_deleted_number(arr, mixed_arr):
    # Your code here
    ret = 0
    for i in arr:
        if i not in mixed_arr:
            ret = i

    return ret
