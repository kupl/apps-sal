def count_positives_sum_negatives(arr):
    if len(arr) == 0:
        return []
    positives = list(filter(lambda x: x>0, arr))
    negatives = list(filter(lambda x: x<0, arr))
    return [len(positives),sum(negatives)]
