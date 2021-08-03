def jumping(arr, n):
    ind = 0
    while ind < len(arr):
        here = arr[ind]
        if here < n:
            arr[ind] += 1
        if here >= n:
            arr[ind] -= 1
        ind += here

    return len([i for i in arr if i == n])
