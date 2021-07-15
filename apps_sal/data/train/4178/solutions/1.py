def min_sum(arr):
    arr.sort()
    left, right, res = 0, len(arr) - 1, 0
    while left < right:
        res += arr[left] * arr[right]
        left += 1
        right -= 1
    return res
