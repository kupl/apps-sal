def yes_no(arr, x=0):
    if len(arr) <= 1: return arr
    return arr[x::2] + yes_no(arr[1-x::2], x+len(arr)&1)
