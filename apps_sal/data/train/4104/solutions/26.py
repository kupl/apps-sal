def max_tri_sum(numbers):
    return sum(sorted(set(numbers), reverse=True)[0:3])
