def count_positives_sum_negatives(arr):
    n_array = []
    count = 0
    sum = 0
    for i in arr:
        if i > 0:
            count += 1
        if i < 0:
            sum += i
    n_array.append(count)
    n_array.append(sum)
    if arr == []:
        return []
    elif arr == [0, 0]:
        return [0, 0]
    return n_array
