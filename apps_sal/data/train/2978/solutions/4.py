def count_sel(lst):
    r = [len(lst), len(set(lst)), sum(lst.count(i) == 1 for i in set(lst))]
    rm = max(lst.count(i) for i in set(lst))
    rv = sorted(i for i in set(lst) if lst.count(i) == rm)
    r.append([rv, rm])
    return r
