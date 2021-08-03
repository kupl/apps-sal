def remove_nth_element(lst, n):
    lst_copy = lst[:]
    del lst_copy[n]
    return lst_copy
