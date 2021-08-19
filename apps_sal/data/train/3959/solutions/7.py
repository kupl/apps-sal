def max_sum(arr, ranges):
    results = []
    for r in ranges:
        partialSum = 0
        for j in range(r[0], r[1] + 1):
            partialSum += arr[j]
        results.append(partialSum)
    return max(results)
