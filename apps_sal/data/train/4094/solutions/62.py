def count_positives_sum_negatives(arr):
    count_pos = 0
    sum_neg = 0
    for num in arr:
        if num > 0:
            count_pos += 1
        if num < 0:
            sum_neg += num
    return [count_pos] + [sum_neg] if arr else []
