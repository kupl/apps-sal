def max_tri_sum(numbers):
    return sum(sorted(set(numbers), key=None, reverse=True)[:3])
