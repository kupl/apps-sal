def count_positives_sum_negatives(arr):
    if arr is None or len(arr) == 0:
        return []
    non_positives = [x for x in arr if x < 1]
    count_positives = len(arr) - len(non_positives)
    sum_negatives = sum(non_positives)
    return [count_positives, sum_negatives]
