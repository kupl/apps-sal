def is_sorted_and_how(arr):
    brr = arr.copy()
    crr = arr.copy()
    brr.sort()
    crr.sort(reverse=True)

    if arr == brr:
        return 'yes, ascending'
    if arr == crr:
        return 'yes, descending'
    else:
        return 'no'
