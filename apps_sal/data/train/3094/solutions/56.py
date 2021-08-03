def sum_array(arr):
    try:
        if len(arr) == 1:
            return 0
        return sum(arr) - max(arr) - min(arr)
    except:
        return 0
