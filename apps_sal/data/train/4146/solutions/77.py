def is_sorted_and_how(arr):
    if sorted(arr) == arr:
        return "yes, ascending"
    return "yes, descending" if sorted(arr, reverse=True) == arr else "no"
