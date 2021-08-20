def is_sorted_and_how(arr):
    if sorted(arr) != arr and sorted(arr)[::-1] != arr:
        return 'no'
    return 'yes, ascending' if sorted(arr) == arr else 'yes, descending'
