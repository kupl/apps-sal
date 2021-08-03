def jumping_number(number):
    nums = [int(i) for i in str(number)]
    n = len(nums)
    for i in range(n - 1):
        if abs(nums[i] - nums[i + 1]) != 1:
            return 'Not!!'
    return 'Jumping!!'
