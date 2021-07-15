def sum_array(arr):
    if not arr or len(arr) == 1:
        return 0
    else:
        return sum(arr) - min(arr) - max(arr)
