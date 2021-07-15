def cube_odd(arr):
    res_arr = [x for x in arr if isinstance(x, int) and not isinstance(x, bool)]
    if len(res_arr) == len(arr):
        return sum([x**3 for x in arr if x % 2 != 0])
    else:
        return None
