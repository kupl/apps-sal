def is_sorted_and_how(list):
    if list == sorted(list):
        return("yes, ascending")
    if list == sorted(list, reverse=True):
        return("yes, descending")
    else:
        return("no")
