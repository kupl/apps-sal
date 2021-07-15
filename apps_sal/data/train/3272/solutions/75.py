def find_average(nums):
    sum = 0
    n = 0
    for i in nums:
        sum += i
        n += 1
    if n > 0:
        return sum / n
    else:
        return 0
