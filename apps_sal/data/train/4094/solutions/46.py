def count_positives_sum_negatives(arr):
    count = 0
    summ = 0
    if len(arr) == 0:
        return []
    else:
        for i in arr:
            if i > 0:
                count += 1
            else:
                summ += i
        return [count, summ]
