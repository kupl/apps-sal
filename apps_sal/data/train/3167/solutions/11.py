def twos_difference(lst):
    new_list = []
    lst.sort()
    for (ind, val) in enumerate(lst):
        get_check = val + 2
        try:
            if lst.index(get_check):
                new_list.append((val, get_check))
        except ValueError:
            continue
    return new_list
