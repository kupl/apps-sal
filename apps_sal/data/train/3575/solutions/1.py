def powerset(nums):
    if not nums:
        return [[]]
    l = powerset(nums[1:])
    a = nums[0]
    return l + [[a] + q for q in l]
