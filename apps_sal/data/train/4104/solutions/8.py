def max_tri_sum(numbers):
    return sum(sorted([x for x in set(numbers)])[-3:])
