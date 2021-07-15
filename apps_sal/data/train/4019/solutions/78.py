def max_multiple(divisor, bound):
    nums = list(range(1, bound + 1))
    nums = reversed(nums)
    for n in nums:
        if n % divisor == 0:
            return n
    

