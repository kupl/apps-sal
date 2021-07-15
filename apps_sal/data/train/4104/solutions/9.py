def max_tri_sum(numbers):
    n = sorted(list(set(numbers)),reverse=True)
    return sum(n[:3])
