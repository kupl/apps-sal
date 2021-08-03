def max_tri_sum(numbers):
    a = sorted(list(set(numbers)), reverse=True)
    return sum(a[:3])
