def min_unfairness(arr,k):
    arr = sorted(arr)
    return min(b - a for a, b in zip(arr, arr[k-1:])) if arr and k else 0
