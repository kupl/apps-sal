def count_positives_sum_negatives(arr):
    return ([], [len([x for x in arr if x > 0]), sum(x for x in arr if x < 0)])[len(arr) != 0]
