def find_deleted_number(arr, mixed_arr):
    # Works only if exactly one number is missing
    return sum(arr) - sum(mixed_arr)
