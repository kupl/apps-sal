def find_average(nums):
    total = 0
    if len(nums) > 0:
        for i in nums:
            total += i
        le = len(nums)
        print(total / le)
        return total / le
    else:
        return 0
