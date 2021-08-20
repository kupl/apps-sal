def find_average(nums):
    if nums == []:
        return 0
    else:
        x = 0
        for i in nums:
            x = i + x
        y = x / len(nums)
    return y
