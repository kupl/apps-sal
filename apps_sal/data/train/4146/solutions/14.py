def is_sorted_and_how(arr):
    arrS = sorted(arr)
    revArrS = sorted(arr, reverse = True)
    if arr == arrS:
        return "yes, ascending"
    elif arr == revArrS:
        return "yes, descending"
    else:
        return "no"
