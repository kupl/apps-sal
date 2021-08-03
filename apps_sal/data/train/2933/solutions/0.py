def solve(nums, div):
    return [x + x % div for x in nums]
