def find_smallest_int(arr):
    # Code here
    ans = arr[0]
    for x in arr:
        if x < ans:
            ans = x
    return ans
