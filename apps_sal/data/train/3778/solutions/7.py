def find_smallest_int(arr):
    currentSmallest = arr[0]
    for x in range (len(arr)):
        if currentSmallest > arr[x]:
            currentSmallest = arr[x]
    return currentSmallest

