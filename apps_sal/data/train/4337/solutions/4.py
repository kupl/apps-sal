def swap_head_tail(arr):
    middle, odd = divmod(len(arr), 2)
    return arr[middle + odd:] + arr[middle:middle + odd] + arr[:middle]
