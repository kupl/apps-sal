def is_sorted_and_how(arr):
    
    new_sorted_list = sorted(arr)
    new_sorted_list_d = sorted(arr, reverse = True)
    
    if arr == new_sorted_list:
        return "yes, ascending"
    elif arr == new_sorted_list_d:
        return "yes, descending"
    else:
        return "no"
