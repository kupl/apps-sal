def sum_of_intervals(intervals): 
    s = []
    for i in intervals:
        s += list(range(i[0],i[1]))
    return len(set(s))
