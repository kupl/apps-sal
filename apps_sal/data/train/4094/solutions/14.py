def count_positives_sum_negatives(arr):
    if not arr:
        return([])
    else:
        pos = sum(int>0 for int in arr)
        neg = sum(int for int in arr if int < 0)
        return([pos,neg])
