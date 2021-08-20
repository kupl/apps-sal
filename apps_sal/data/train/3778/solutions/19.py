def find_smallest_int(arr):
    ans = arr[0]
    for x in arr:
        if x < ans:
            ans = x
    return ans
