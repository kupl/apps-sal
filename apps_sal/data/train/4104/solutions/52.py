def max_tri_sum(numbers):
    v = sorted(set(numbers))
    return sum(v[-3:])
