def count_positives_sum_negatives(arr):    
    return [] if arr == None or arr == [] else [len(list(filter(lambda x: x > 0, arr))), sum(filter(lambda x: x < 0, arr))]
