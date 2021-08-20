def summary_ranges(nums):
    (i, lst, nums) = (0, [], sorted(set(nums)))
    while i < len(nums):
        (i, j) = (i + 1, i)
        while i < len(nums) and nums[i] == nums[i - 1] + 1:
            i += 1
        lst.append(str(nums[j]) if j + 1 == i else '{}->{}'.format(nums[j], nums[i - 1]))
    return lst
