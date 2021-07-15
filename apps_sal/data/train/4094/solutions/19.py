def count_positives_sum_negatives(arr):
    if not arr:
        return []
    
    count = len(arr)
    sum = 0
    for num in arr:
        if num <= 0:
            count -= 1
            sum += num
    return [count, sum]

