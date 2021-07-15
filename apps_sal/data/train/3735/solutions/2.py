def find_missing_numbers(arr):
    return [n for n in range(arr[0], arr[-1]) if n not in arr] if arr else []
