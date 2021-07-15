def knapsack(capacity, items):
    liste = sorted([ x+(i,) for i,x in enumerate(items)], key= lambda x: x[1]/x[0], reverse = True)
    result = [0]*len(items)
    for s,v,i in liste :
        if capacity >= s :
            result[i] = int(capacity/s)
            capacity -= result[i]*s
    return result
