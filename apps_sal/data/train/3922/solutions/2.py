def jumping(arr, n):
    (l, pos) = (len(arr), 0)
    while pos < l:
        (arr[pos], pos) = (arr[pos] + (arr[pos] < n or -1), pos + arr[pos])
    return arr.count(n)
