def sum_array(arr):
    if not arr:
        return 0
    else:
        res = sorted(arr)[1:-1]
        return sum((i for i in res))
