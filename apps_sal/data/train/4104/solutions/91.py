def max_tri_sum(numbers):
    x = sorted(list(set(numbers)), reverse=True)
    return sum(x[:3])
