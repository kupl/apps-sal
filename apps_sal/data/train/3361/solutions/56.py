def sum_of_minimums(numbers):
    sum1=0
    for nums in numbers:
        sum1+=min(nums)
    return sum1
