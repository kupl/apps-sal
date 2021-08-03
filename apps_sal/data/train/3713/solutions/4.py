def find_deleted_number(arr, mixed_arr):
    return 0 if not arr else arr[-1] * (arr[-1] + 1) / 2 - sum(mixed_arr)
