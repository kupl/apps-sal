def count_positives_sum_negatives(arr):
    if arr.__len__() == 0:
        return []
    else:
        (sum_value, count) = (0, 0)
        for value in arr:
            if value < 0:
                sum_value += value
            elif value > 0:
                count += 1
            else:
                continue
        return [count, sum_value]
