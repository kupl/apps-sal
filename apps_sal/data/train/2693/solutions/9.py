def remove_nth_element(lst, n):
    return [j for i, j in enumerate(lst) if n != i]
