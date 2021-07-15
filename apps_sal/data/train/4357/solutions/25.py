import heapq

def nth_smallest(nlist, num):
    return(heapq.nsmallest(num, nlist))[-1]
