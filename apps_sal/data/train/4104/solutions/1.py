from heapq import nlargest

def max_tri_sum(numbers):
    return sum(nlargest(3, set(numbers)))
