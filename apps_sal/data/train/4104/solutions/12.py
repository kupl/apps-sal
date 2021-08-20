def max_tri_sum(numbers):
    return sum(__import__('heapq').nlargest(3, set(numbers)))
