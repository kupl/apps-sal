def without_last(lst):
    lst_copy = list(lst)  # creates a shallow copy
    lst_copy.pop()
    return lst_copy

# There are several other ways to solve this
# like returning lst[:-1] directly or creating a new list iteratively with all the elements of lst minus the last one
