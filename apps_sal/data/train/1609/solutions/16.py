def sum_of_intervals(intervals):
    list1=[]
    for i in intervals:
        for j in range(i[0],i[1]):
            list1.append(j)
    set1=set(list1)
    return len(set1)
