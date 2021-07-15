def sum_array(arr):
    return 0 if (not arr or len(arr) <= 1) else sum(sorted(arr)[1:-1])
