def sel_reverse(arr, l):
    return sum([arr[i:i + l][::-1] for i in range(0, len(arr), l)], []) if l > 0 else arr
