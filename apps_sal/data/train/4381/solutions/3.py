def min_unfairness(arr, k):
    # your code here
    if k < 2 or len(arr) < 2:
        return 0

    arr.sort()


#    return min([(arr[k+i-1]-arr[i]) for i in range(len(arr)-k+1)])
    mindist = float('inf')

    for i in range(len(arr) - k + 1):
        dist = arr[k + i - 1] - arr[i]

        if dist < mindist:
            mindist = dist

    return mindist
