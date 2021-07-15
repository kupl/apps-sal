def find_average(nums):
    if len(nums) == 0:
        return 0
    sum=0
    for num in nums:
        sum+=num
    return sum/len(nums)
