def largest_pair_sum(numbers):
    from heapq import nlargest
    return sum(nlargest(2, numbers))
