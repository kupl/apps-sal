def find_average(nums):
    average = 0
    sum_nums = 0
    count_nums = 0
    for num in nums:
        sum_nums += num
        count_nums += 1
        average = (sum_nums / count_nums)
    return average
