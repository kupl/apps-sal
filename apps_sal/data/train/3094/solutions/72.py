def sum_array(arr):
    return 0 if not bool(arr) or len(arr) < 3 else sum(sorted(arr)[1:-1])
