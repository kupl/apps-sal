def min_unfairness(arr, k):

    if not arr or k == 0:
        return 0
    arr.sort()

    min_unf = float('inf')

    for i in range(len(arr) - k + 1):

        subarr_min = arr[i]
        subarr_max = arr[i + k - 1]

        min_unf = min(min_unf, subarr_max - subarr_min)

    return min_unf
