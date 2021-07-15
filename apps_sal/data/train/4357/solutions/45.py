from heapq import nsmallest

def nth_smallest(a,p):
    return nsmallest(p,a)[-1]
