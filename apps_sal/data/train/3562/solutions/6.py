from collections import deque


def count_inversion(nums):
    forward_nums = deque(nums)
    result = 0
    for a in nums:
        forward_nums.popleft()
        for b in forward_nums:
            if a > b:
                result += 1
    return result
