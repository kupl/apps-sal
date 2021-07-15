def is_sorted_and_how(arr):
    asc = True
    desc = True
    for i in range(1, len(arr)):
        if arr[i-1] == arr[i]:
            return 'no'
        if arr[i - 1] < arr[i]:
            desc = False
        else:
            asc = False
        if not asc and not desc:
            return 'no'
    return  'yes, ascending' if asc else 'yes, descending'
