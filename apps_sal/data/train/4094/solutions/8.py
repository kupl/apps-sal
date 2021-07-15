def count_positives_sum_negatives(arr):
    
    if arr == [] : return []
    
    result = [0, 0]
    
    for value in arr:
        if value > 0:
            result[0] += 1
        else:
            result[1] += value
        
    return result
