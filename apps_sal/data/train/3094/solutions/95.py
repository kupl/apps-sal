def sum_array(arr):
    try:
        l = arr.remove(min(arr))
        l = arr.remove(max(arr))
        return sum(arr)
    except:
        return 0
