def find_outlier(nums):
    base_parity = sum((x % 2 for x in nums[:3])) // 2
    for i in range(len(nums)):
        if nums[i] % 2 != base_parity:
            return nums[i]
