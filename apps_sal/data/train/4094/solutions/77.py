def count_positives_sum_negatives(arr):
    if not arr:
        return []
    sum_of_negative = 0
    positive_num = 0
    for i in arr:
        if i <= 0:
            sum_of_negative += i
        else:
            positive_num += 1
    return [positive_num, sum_of_negative]
            

