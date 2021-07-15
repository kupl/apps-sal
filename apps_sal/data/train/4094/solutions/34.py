def count_positives_sum_negatives(arr):
    #your code here
    res = []
    if arr:
        i = 0
        j = 0
        for num in arr:
            if num > 0:
                i = i+1
            else:
                j = num+j
        res = [i,j]  
    return res

