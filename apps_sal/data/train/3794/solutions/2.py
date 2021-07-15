import random

def partition(vector, left, right, pivotIndex):
    pivotValue = vector[pivotIndex]
    vector[pivotIndex], vector[right] = vector[right], vector[pivotIndex]  # Move pivot to end
    storeIndex = left
    for i in range(left, right):
        if vector[i] < pivotValue:
            vector[storeIndex], vector[i] = vector[i], vector[storeIndex]
            storeIndex += 1
    vector[right], vector[storeIndex] = vector[storeIndex], vector[right]  # Move pivot to its final place
    return storeIndex

def select(vector, left, right, k):
    "Returns the k-th smallest, (k >= 0), element of vector within vector[left:right+1] inclusive."
    if k < len(vector):
        while True:
            pivotIndex = random.randint(left, right)     # select pivotIndex between left and right
            pivotNewIndex = partition(vector, left, right, pivotIndex)
            pivotDist = pivotNewIndex - left
            if pivotDist == k:
                return vector[pivotNewIndex]
            elif k < pivotDist:
                right = pivotNewIndex - 1
            else:
                k -= pivotDist + 1
                left = pivotNewIndex + 1

def nth_smallest(arr, n):
    unique = list(set(arr))
    return select(unique, 0, len(unique)-1, n-1)
