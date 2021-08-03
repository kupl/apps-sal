def remove_nth_element(lst, n):
    # Fix it
    import copy
    lst_copy = copy.deepcopy(lst)
    del lst_copy[n]
    return lst_copy
