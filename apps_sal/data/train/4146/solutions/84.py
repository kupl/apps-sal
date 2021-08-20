def is_sorted_and_how(arr):
    h = arr.copy()
    h.sort(reverse=True)
    p = arr.copy()
    p.sort()
    if arr == p:
        return 'yes, ascending'
    if arr == h:
        return 'yes, descending'
    else:
        return 'no'
