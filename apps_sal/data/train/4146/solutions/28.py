def is_sorted_and_how(arr):
    ascending = sorted(arr)
    descending = sorted(arr, reverse=True)
    if arr == ascending:
        return "yes, ascending"
    if arr == descending:
        return "yes, descending"
    return 'no'
