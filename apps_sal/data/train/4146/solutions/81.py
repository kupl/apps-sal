def is_sorted_and_how(arr):
    sort = sorted(arr)
    return "yes, ascending" if arr == sort else "yes, descending" if arr == sort[::-1] else "no"
