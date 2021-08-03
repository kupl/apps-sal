def find_deleted_number(arr, mixed_arr):
    lost = 0
    for i in arr:
        if i not in mixed_arr:
            lost = i

    return lost
