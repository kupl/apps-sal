def sum_of_minimums(numbers):
    total = 0
    for nums in numbers:
        total += min(nums)
    return total
