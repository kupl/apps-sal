def remove_nth_element(lst, n):
    # Fix it
    lst_copy = lst[:]
    del lst_copy[n]
    return lst_copy

remove_nth_element=lambda a,n:a[:n]+a[n+1:]
