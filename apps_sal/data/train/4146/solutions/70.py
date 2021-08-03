def is_sorted_and_how(arr):
    if arr[0] > arr[1]:
        try:
            if arr[1] < arr[2]:
                return 'no'
        except:
            pass
        return "yes, descending"
    elif arr[0] < arr[1]:
        try:
            if arr[1] > arr[2]:
                return 'no'
        except:
            pass
        return "yes, ascending"
    return 'no'
