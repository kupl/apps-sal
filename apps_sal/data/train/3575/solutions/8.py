def powerset(nums):
    l = len(nums)
    return [[x for (j, x) in enumerate(nums) if i & 1 << l - j - 1] for i in range(2 ** l)]
