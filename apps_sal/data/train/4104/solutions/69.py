def max_tri_sum(numbers):
    return sum(sorted(set(list(numbers)))[-3:])
