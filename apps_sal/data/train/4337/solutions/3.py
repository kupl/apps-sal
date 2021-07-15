def swap_head_tail(arr):
    m = len(arr) // 2
    return arr[-m:] + arr[m:-m] + arr[:m]
