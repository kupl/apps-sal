def sum_of_intervals(intervals):
    #1) get range of each tuplem -> list
    #2) turn "list" obj into "set" obj to remove repeats
    #3) return the length of the final "set" obj
    return len(set([i for t in intervals for i in range(t[0],t[-1])]))
