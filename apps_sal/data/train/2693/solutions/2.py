def remove_nth_element(lst, n):
    import copy
    lst_copy = copy.deepcopy(lst)
    del lst_copy[n]
    return lst_copy
