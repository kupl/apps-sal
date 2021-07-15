def max_tri_sum(numbers):
    return sum(sorted([item for item in set(numbers)])[-3:])
