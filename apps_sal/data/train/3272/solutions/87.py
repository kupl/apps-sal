def find_average(nums):
    n = 0
    for n in nums:
        n = sum(nums) / len(nums)
    if len(nums) == 0:
        print('Error')
    else:
        print(n)
    return n
