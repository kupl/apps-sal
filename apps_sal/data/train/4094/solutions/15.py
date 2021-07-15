def count_positives_sum_negatives(arr):
    if not arr:
        return []
    else: 
        x = sum(1 for i in arr if i>= 1)     
        y = sum(i for i in arr if i < 1)
        return [x, y]
