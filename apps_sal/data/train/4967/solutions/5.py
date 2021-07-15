def knapsack(capacity, items):
    arr = sorted(enumerate(items), key = lambda x: x[1][1]/x[1][0], reverse = True)
    sack = [0]*len(items)
    
    for j, (w, v) in arr:
        if w <= capacity:
            sack[j], capacity = divmod(capacity, w)
    
    return sack
