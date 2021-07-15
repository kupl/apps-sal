def is_sorted_and_how(arr):
    if arr[::-1] == sorted(arr):
        return "yes, descending"
    if arr == sorted(arr):
        return "yes, ascending"
    if arr != sorted(arr):
        return "no"

