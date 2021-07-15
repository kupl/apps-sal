def max_product(lst, n_largest_elements):
    accumulator = 1
    lst.sort()
    if len(lst) == 0:
        return lst[0]
    else:
        x = lst[-n_largest_elements:]
        for eachnumber in x:
            accumulator = accumulator * eachnumber
        return accumulator
