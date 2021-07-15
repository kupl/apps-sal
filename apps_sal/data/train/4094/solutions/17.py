def count_positives_sum_negatives(arr):
    return [len([x for x in arr if x > 0]), sum(filter(lambda x: x < 0, arr))] if len(arr) != 0 else []
