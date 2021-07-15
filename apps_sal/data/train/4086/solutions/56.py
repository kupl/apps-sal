def first_non_consecutive(arr):
    numbers = list(range(arr[0], arr[-1] + 1))
    missing = [number for number in numbers if number not in arr]
    return missing[0] + 1 if missing != [] else None
