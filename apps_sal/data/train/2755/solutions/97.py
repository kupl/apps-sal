def multiple_of_index(arr):
    res = []
    for (idx, elem) in enumerate(arr):
        if idx != 0:
            if elem % idx == 0:
                res.append(elem)
    return res
