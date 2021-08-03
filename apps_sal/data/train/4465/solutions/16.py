def super_size(num):
    res = [x for x in str(num)]
    Sorted_res = sorted(res, reverse=True)
    Sorted_string = ''.join(Sorted_res)
    return int(Sorted_string)
