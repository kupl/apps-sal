def count_positives_sum_negatives(arr):
    if arr == []:
        return []
        
    pos = sum([i>0 for i in arr])
    neg = sum(i for i in arr if i< 0)
    
    return [pos,neg]

