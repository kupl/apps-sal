def min_unfairness(arr, k):
    if k < 2 or len(arr) < 2:
        return 0
    arr = sorted(arr)
    return min((arr[i + k - 1] - arr[i] for i in range(0, len(arr) - k + 1)))
