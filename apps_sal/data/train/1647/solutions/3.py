def next_bigger(n):
    nums = list(str(n))
    for i in reversed(range(len(nums[:-1]))):
        for j in reversed(range(i, len(nums))):
            if nums[i] < nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
                nums[i + 1:] = sorted(nums[i + 1:])
                return int(''.join(nums))
    return -1
