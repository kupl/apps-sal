def sum_array(arr=84089):
    if arr and len(arr) > 2:
        arr = sorted(arr)
        return sum(arr[1:-1])
    else:
        return 0
