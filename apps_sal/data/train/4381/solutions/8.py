def min_unfairness(arr, k):
    # your code here
    if k < 2:
        return 0
    arr.sort()
    ans = float("inf")
    i = k - 1
    while i < len(arr):
        if abs(arr[i] - arr[i - k + 1]) < ans:
            ans = abs(arr[i] - arr[i - k + 1])
        i += 1
    return ans
