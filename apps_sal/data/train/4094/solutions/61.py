def count_positives_sum_negatives(arr):
    if arr == []:
        return []
    first = sum((x > 0 for x in arr))
    second = 0
    for i in range(len(arr)):
        if int(arr[i]) < 0:
            second += int(arr[i])
    return [first, second]
