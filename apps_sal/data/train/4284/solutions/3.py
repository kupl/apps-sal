def array_leaders(numbers):
    nums = numbers + [0]
    return [a for (c, a) in enumerate(nums, 1) if a > sum(nums[c:])]
