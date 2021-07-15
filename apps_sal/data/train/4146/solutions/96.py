def is_sorted_and_how(arr):
    my_list = list(arr)
    if sorted(my_list) == arr:
        return "yes, ascending"
    elif sorted(my_list, reverse = True) == arr:
        return "yes, descending"
    else:
        return "no"
