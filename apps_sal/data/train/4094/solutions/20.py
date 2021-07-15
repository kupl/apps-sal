def count_positives_sum_negatives(arr):
    if not arr:
        return arr
    count = 0
    su = []
    for i in arr:
        if i > 0:
            count += 1
        else:
            su.append(i)
    return [count, sum(su)]
