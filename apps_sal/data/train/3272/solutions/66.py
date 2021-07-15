def find_average(nums):
    try:
        accumulator = 0
        for eachnumber in nums:
            accumulator = accumulator + eachnumber
        return accumulator / len(nums)
    except ZeroDivisionError as zero_error:
        return 0
