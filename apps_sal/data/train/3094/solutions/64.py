def sum_array(arr):
    if not arr or len(arr) in [1, 2]:
        return 0
    (maxn, minn, sumn) = (arr[0], arr[0], 0)
    for n in arr:
        if n > maxn:
            maxn = n
        elif n < minn:
            minn = n
        sumn += n
    return sumn - maxn - minn
