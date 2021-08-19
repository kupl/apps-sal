def is_sorted_and_how(arr):
    arrasc = arr[:]
    arrasc.sort()
    arrdsc = arr[:]
    arrdsc.sort(reverse=True)
    if arrasc == arr:
        return 'yes, ascending'
    elif arrdsc == arr:
        return 'yes, descending'
    else:
        return 'no'
