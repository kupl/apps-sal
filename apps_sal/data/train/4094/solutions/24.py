def count_positives_sum_negatives(arr):
    if len(arr) == 0:
        return []
    count_positive = 0
    sum_negative = 0
    for i in range(len(arr)):
        if arr[i] > 0:
            count_positive = count_positive + 1
        else:
            sum_negative = sum_negative + arr[i]
    return [count_positive, sum_negative]
