def solve(nums, div):
    for x in range(0, len(nums)):
        nums[x] += nums[x] % div
    return nums
