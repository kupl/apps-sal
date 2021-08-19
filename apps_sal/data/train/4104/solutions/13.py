def max_tri_sum(numbers):
    # your code here
    ls = sorted(list(set(numbers)))
    return ls[-1] + ls[-2] + ls[-3]
