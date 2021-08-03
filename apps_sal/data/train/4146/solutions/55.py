def is_sorted_and_how(arr):

    if arr == sorted(arr):
        return "yes, ascending"
    elif arr[0] > arr[-1]:
        return "yes, descending"
    else:
        return "no"
