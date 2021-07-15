def sequence_classifier(arr):
    unordered = True
    strictly_increasing = True
    not_decreasing = True
    strictly_decreasing = True
    not_increasing = True
    constant = True
    for i in range(1,len(arr)):
        if arr[i-1] != arr[i]:
            constant = False
        if arr[i-1] <= arr[i]:
           strictly_decreasing = False
        if arr[i-1] >= arr[i]:
            strictly_increasing = False
        if not arr[i-1] <= arr[i]:
           not_decreasing = False
        if not arr[i-1] >= arr[i]:
            not_increasing = False
    if constant:
        return 5
    if strictly_decreasing:
        return 3
    if strictly_increasing:
        return 1
    if not_increasing:
        return 4
    if not_decreasing:
        return 2
    return 0
