def remove_nth_element(lst, n):
    lst_copy = lst.copy()
    del lst_copy[n]
    return lst_copy
