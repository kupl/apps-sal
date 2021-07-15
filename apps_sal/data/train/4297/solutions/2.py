def get_mean(arr, x, y):
    l = len(arr)
    if 1 < x <= l and 1 < y <= l:
        mx = sum(arr[:x]) / x
        my = sum(arr[-y:]) / y
        return (mx + my) / 2
    else:
        return -1

