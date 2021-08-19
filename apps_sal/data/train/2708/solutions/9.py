def yes_no(arr):
    r = []
    for i in range(0, len(arr) * 2 - 1, 2):
        r.append(arr[i])
        if i < len(arr) - 1:
            arr.append(arr[i + 1])
    return r
