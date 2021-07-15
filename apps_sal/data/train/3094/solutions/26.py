def sum_array(arr):
    if not arr or len(arr) <= 2:
        return 0
    else:
        arr.sort()
        return sum(arr[1:-1])
