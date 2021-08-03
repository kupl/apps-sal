def min_sum(arr):
    # Your code here
    ans = 0
    while len(arr) > 0:
        ans += max(arr) * min(arr)
        arr.remove(max(arr))
        arr.remove(min(arr))
    return ans
