def missing(nums, s):
    s = s.lower().replace(' ', '')
    nums = sorted(nums)
    return 'No mission today' if any((i >= len(s) for i in nums)) else ''.join((s[i] for i in nums))
