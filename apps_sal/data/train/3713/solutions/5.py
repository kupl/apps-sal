def find_deleted_number(arr, mixed_arr):
    return len(arr) > len(mixed_arr) and (set(arr) - set(mixed_arr)).pop()
