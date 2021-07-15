def iq_test(numbers):
    nums = [int(n) % 2 for n in numbers.split()]
    if sum(nums) == 1:
        return nums.index(1) + 1
    else:
        return nums.index(0) + 1
