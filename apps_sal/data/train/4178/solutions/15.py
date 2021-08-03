def min_sum(arr):
    a = sorted(arr)
    if len(a) == 0:
        return 0
    return (a[0] * a[-1]) + min_sum(a[1:-1])
