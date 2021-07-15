def find_average(nums):
    s = 0
    if nums == []:
        return 0
    else:
        for i in range(len(nums)):
            s = s + nums[i]
        return s/len(nums)
