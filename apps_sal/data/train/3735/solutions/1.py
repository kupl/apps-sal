def find_missing_numbers(arr):
    return [x for x in range(arr[0], arr[-1] + 1) if x not in arr] if arr else []
