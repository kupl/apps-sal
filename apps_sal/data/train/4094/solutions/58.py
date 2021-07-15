def count_positives_sum_negatives(arr):
    
    if not arr or not len(arr):
        return []
    
    p, n = 0, 0
    for e in arr:
        p, n = (p + 1, n) if e > 0 else (p, n + e)
        
    return [p, n]
