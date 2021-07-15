def jumping(arr, n):
    ind = 0
    add = 0
    while ind < len(arr):
        if arr[ind] >= n:
            add = -1
        else:
            add = 1
        arr[ind] += add
        ind += arr[ind] - add
    return arr.count(n)
