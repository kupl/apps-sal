def cube_odd(arr):
    int_arr = []
    for i in arr:
        if type(i) == int:
            int_arr.append(i)
        else:
            return None
    res = []
    for i in int_arr:
        if i % 2 != 0:
            res.append(i)
    res2 = []
    for i in res:
        res2.append(i * i * i)
    return sum(res2)
