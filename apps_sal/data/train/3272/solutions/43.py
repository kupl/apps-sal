def find_average(nums):
    sum = 0
    if not nums:
        return sum
    else:
        for num in nums:
            sum = sum + num
        average = sum / len(nums)
        return average
