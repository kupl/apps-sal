def list_to_array(lst):
    res = []
    while lst:
        res.append(lst.value)
        lst = lst.__next__
    return res

