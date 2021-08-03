def max_tri_sum(numbers):
    a = sorted(set(numbers), reverse=True)
    b = a[:3]
    return sum(b)
