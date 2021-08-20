def summary_ranges(nums):
    nums.append(float('inf'))
    (i, result) = (nums[0], [])
    for (j, n) in zip(nums, nums[1:]):
        if n - j > 1:
            result.append(str(i) if i == j else f'{i}->{j}')
            i = n
    return result
