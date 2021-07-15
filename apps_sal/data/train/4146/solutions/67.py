def is_sorted_and_how(arr):
    lst = arr[:]
    lst.sort()
    if lst == arr:
        return 'yes, ascending'
    elif lst[::-1] == arr:
        return 'yes, descending'
    else:
        return 'no'
