def find(nums):
    return (min(nums) + max(nums)) * (len(nums) + 1) / 2 - sum(nums)
