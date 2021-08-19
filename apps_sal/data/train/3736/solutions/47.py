def minimum(arr):
    currentSmallest = arr[0]
    for x in range(1, len(arr)):
        if arr[x] < currentSmallest:
            currentSmallest = arr[x]
    return currentSmallest


def maximum(arr):
    currentLargest = arr[0]
    for x in range(1, len(arr)):
        if arr[x] > currentLargest:
            currentLargest = arr[x]
    return currentLargest
