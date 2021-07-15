def find_deleted_number(arr, mixed_arr):
    arr = set(sorted(arr))
    mixed_arr = set(sorted(mixed_arr))
    return 0 if arr == mixed_arr else list(arr.difference(mixed_arr))[0]
