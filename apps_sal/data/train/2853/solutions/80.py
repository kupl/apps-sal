def solve(arr):
    (i, k) = (0, len(arr))
    while k > i:
        if arr.count(arr[i]) != 1:
            del arr[i]
            k -= 1
        else:
            i += 1
    return arr
