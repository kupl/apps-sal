def powerset(nums):
    if len(nums) == 1:
        return [[], nums]
    s = powerset(nums[1:])
    for a in s[:]:
        s.append([nums[0]] + a)
    return s
