def min_unfairness(arr, k):
    if k < 2 or len(arr) < 2:
        return 0

    arr.sort()

    mindist = float('inf')

    for i in range(len(arr) - k + 1):
        dist = arr[k + i - 1] - arr[i]

        if dist < mindist:
            mindist = dist

    return mindist
