def sel_reverse(arr, l):
    # your code here
    res = []

    if l == 0:
        return arr

    i = 0
    while i < len(arr):
        res.append(arr[i:i + l][::-1])
        i += l

    return sum(res, [])
