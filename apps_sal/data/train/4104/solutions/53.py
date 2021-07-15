def max_tri_sum(numbers):
    return sum(sorted(set(numbers),reverse=True)[i] for i in range(3))
