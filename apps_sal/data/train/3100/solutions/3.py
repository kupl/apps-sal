def max_and_min(arr1, arr2):
    arr1.sort()
    arr2.sort()
    i = 0
    difference = []

    while i < len(arr1):
        local = []
        for element in arr2:
            local_dif = abs(arr1[i] - element)
            local.append(local_dif)
        local.sort()
        difference.append(min(local))
        difference.append(max(local))

        i += 1
    difference.sort()
    maximum = max(difference)
    minimum = min(difference)
    return [maximum, minimum]
