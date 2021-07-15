def summary_ranges(nums):
    if not nums:
        return []
    ranges = []
    first = nums[0]
    for current, previous in zip(nums[1:], nums[:-1]):
        if current - previous not in [0, 1]:
            ranges.append((first, previous))
            first = current
    ranges.append((first, nums[-1]))
    return ["{}->{}".format(a, b) if a!=b else str(a) for a, b in ranges]
