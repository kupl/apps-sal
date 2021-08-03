def find_missing_numbers(arr):
    if len(arr):
        return [i for i in range(arr[0], arr[-1]) if i not in arr]
    else:
        return []
