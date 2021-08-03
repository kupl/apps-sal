def array_leaders(nums):
    return [nums[i] for i in range(len(nums)) if nums[i] > sum(nums[i + 1:])]
