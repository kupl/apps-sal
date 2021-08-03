def count_positives_sum_negatives(arr):
    a = [0, 0]
    if not arr:
        return []
    for n in range(0, len(arr)):
        if arr[n] > 0:
            a[0] += 1
        elif arr[n] < 0:
            a[1] += arr[n]
    return a
