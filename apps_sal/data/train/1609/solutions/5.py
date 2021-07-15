def sum_of_intervals(intervals):
    total = set()
    for x,y in intervals:
        for i in range(x,y):
            total.add(i)    
    return(len(total))
