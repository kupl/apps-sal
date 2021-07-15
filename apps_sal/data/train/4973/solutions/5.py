def trouble(nums, target):
    if len(nums) < 2:
        return nums
    result = []
    left = 0
    right = 1
    while True:
        try:
            if nums[left] + nums[right] != target:
                result.append(nums[left])
                left = right
        except LookupError:
            result.append(nums[left])
            break
        right += 1
    return result

