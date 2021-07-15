def is_sorted_and_how(arr):
    
    x = arr[:]
    
    if sorted(x) == arr:
        return "yes, ascending"
    elif sorted(x, reverse=True) == arr:
        return "yes, descending"
    else:
        return "no"
