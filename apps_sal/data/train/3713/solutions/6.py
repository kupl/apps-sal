def find_deleted_number(arr, mixed_arr):
    res = []
    for n in arr:
        if n not in mixed_arr: return n
    return 0
