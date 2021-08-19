def count_positives_sum_negatives(arr):
    if not arr:
        return arr
    (count, sum_) = (0, 0)
    for number in arr:
        if number > 0:
            count += 1
        elif number < 0:
            sum_ += number
    return [count, sum_]
