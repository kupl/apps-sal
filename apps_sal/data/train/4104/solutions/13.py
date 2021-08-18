def max_tri_sum(numbers):
    ls = sorted(list(set(numbers)))
    return ls[-1] + ls[-2] + ls[-3]
