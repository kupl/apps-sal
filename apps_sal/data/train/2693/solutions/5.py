def remove_nth_element(lst, n):
    lst_copy = lst[:]  # That's a shallow copy
    del lst_copy[n]
    return lst_copy
