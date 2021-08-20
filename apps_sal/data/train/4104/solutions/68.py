def max_tri_sum(numbers):
    c = sorted(set(numbers), reverse=True)
    return sum(c[:3])
