def count_positives_sum_negatives(arr):
    if arr == []:
        return []
    c = 0
    a = []
    i = [i for i in arr if i > 0]
    n = [i for i in arr if i < 0]
    a.append(len(i))
    a.append(sum(n))
    return a
