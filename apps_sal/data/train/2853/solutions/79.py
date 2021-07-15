def solve(arr):
    k = 0
    while k < len(arr):
        while arr.count(arr[k]) > 1:
            del arr[k]
            k = 0
        else:
            k += 1

    return arr
