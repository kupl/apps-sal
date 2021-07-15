def powerset(nums):
    if len(nums) == 0:
        return [[]]
    sub = powerset(nums[1:])
    first = nums[:1]
    buffer = []
    for ele in sub:
        buffer.append(first + ele)
    return sub + buffer
