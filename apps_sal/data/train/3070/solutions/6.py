def unique_sum(lst):
    new_lst = []
    for i in lst:
        if not i in new_lst:
            new_lst.append(i)
    return sum(new_lst) if lst else None
