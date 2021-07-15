def is_sorted_and_how(arr):

    asc = True
    desc = True
    
    for idx in range(1, len(arr)):
        if arr[idx] - arr[idx - 1] >= 0:
            asc = asc & True
            desc = desc & False
        else:
            desc = desc & True
            asc = asc & False

    if asc and not desc:
        return "yes, ascending"
    elif desc and not asc:
        return "yes, descending"
    else:
        return "no"
