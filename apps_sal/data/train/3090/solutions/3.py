from heapq import nlargest

def find_2nd_largest(arr):
    two = nlargest(2, {v for v in arr if isinstance(v,int)})
    if len(two)==2: return two[1]
