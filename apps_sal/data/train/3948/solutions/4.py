def sel_reverse(arr, l):
    l = l or 1
    return [
        x
        for i in range(0, len(arr), l)
        for x in reversed(arr[i:i+l])
    ]
