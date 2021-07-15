from heapq import nlargest

def max_tri_sum(numbers):
    assert len(numbers) >= 3
    return sum(nlargest(3, set(numbers)))
