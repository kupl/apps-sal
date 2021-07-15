def first_n_smallest(arr, n):
    lst = sorted(enumerate(arr), key=lambda it: it[1])[:n]
    lst.sort(key=lambda it:it[0])
    return [v for _,v in lst]
