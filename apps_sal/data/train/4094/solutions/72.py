def count_positives_sum_negatives(arr):
    if arr == []:
        return []
    sum = 0
    count = 0
    for number in arr:
        if number < 0:
            sum += number
        if number > 0:
            count += 1
    return [count, sum]
