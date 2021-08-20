def is_sorted_and_how(arr):
    sorted_asc = sorted(arr)
    sorted_desc = sorted_asc[::-1]
    return 'yes, ascending' if sorted_asc == arr else 'yes, descending' if sorted_desc == arr else 'no'
