def solve(nums, div):
    if len(nums) == 0:
        return nums
    index = 0
    for num in nums:
        nums[index] += num % div
        index += 1
    return nums
