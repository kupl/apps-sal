def is_sorted_and_how(arr):
    if arr == sorted(arr):
           return str("yes, ascending")
           
    elif arr == sorted(arr, reverse=True):
           return str("yes, descending")
           
    return str("no")
