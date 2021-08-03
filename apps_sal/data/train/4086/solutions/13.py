def first_non_consecutive(arr):
    for x in range(min(arr), max(arr) + 1):
        if x not in arr:
            return x + 1
