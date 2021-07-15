def find_missing_numbers(arr):
    if len(arr) < 2:
        return []
    return sorted(set(list(range(min(arr), max(arr)))) - set(arr))
