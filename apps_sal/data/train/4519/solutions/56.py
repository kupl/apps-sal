def max_number(n):
    s = str(n)
    nums = []
    for i in range(len(s)):
        nums.append(int(s[i]))
    s = ''
    for i in range(len(nums)):
        for j in range(len(nums) - i - 1):
            if nums[j] <= nums[j + 1]:
                (nums[j], nums[j + 1]) = (nums[j + 1], nums[j])
    for i in nums:
        s += str(i)
    return int(s)
