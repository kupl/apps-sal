def sum_of_intervals(intervals):
    intervals.sort()
    x = 0
    while x < len(intervals) -1:
        if intervals[x][0] <= intervals[x+1][0] and intervals[x][1] >= intervals[x+1][1]:
            intervals.pop( x+1)
        elif intervals[x][0] <= intervals[x+1][0] and intervals[x][1] >= intervals[x+1][0] and intervals[x][1] < intervals[x+1][1]:
            intervals[x] = (intervals[x][0], intervals[x+1][1])
            intervals.pop(x+1)
        else:
            x+=1

    return sum(intervals[x][1] - intervals[x][0] for x in range(len(intervals)))
