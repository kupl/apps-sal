def count_positives_sum_negatives(arr):
    # your code here
    negsum = 0
    positive = 0
    for i in arr:
        if i > 0:
            positive += 1
        elif i < 0:
            negsum += i
    if arr == []:
        return arr
    else:
        return [positive, negsum]
