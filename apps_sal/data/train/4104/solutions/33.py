def max_tri_sum(nums):
    return sum(sorted(list(set(nums)))[-3:])
